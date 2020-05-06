from flask import Flask, render_template, request, session
from hashlib import sha256
import sys
import pathlib
import logging.config
import event_mapper
import users_mapper

import key

app = Flask(__name__)
app.secret_key = key.SECRET_KEY

# ログ設定ファイルからログ設定を読み込み
logging.config.fileConfig('/app/src/log/log.conf')
logger = logging.getLogger()
PASS_WORD = 2

@app.route("/top")
def top():
    status = request.args.get("status")
    return render_template("top.html",status=status)

@app.route("/newcomer")
def newcomer():
    status = request.args.get("status")
    return render_template("newcomer.html",status=status)

@app.route("/registar",methods=["post"])
def registar():
    user_name = request.form["user_name"]
    login_user = users_mapper.select_user(user_name=user_name)
    if login_user:
        return render_template("newcomer.html", status="exist_user")
    else:
        password = request.form["password"]
        hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
        users_mapper.insert_user(user_name, hashed_password)
        session["user_name"] = user_name
        return home()

@app.route("/login",methods=["post"])
def login():
	user_name = request.form["user_name"]
	login_user = users_mapper.select_user(user_name=user_name)
	if login_user:
		password = request.form["password"]
		hashed_password = sha256((user_name + password + key.SALT).encode("utf-8")).hexdigest()
		if login_user[PASS_WORD] == hashed_password:
			session["user_name"] = user_name
			return home()
		else:
			return render_template('top.html', status="wrong_password")
	else:
		return render_template('top.html', status="user_notfound")

@app.route("/logout")
def logout():
    session.pop("user_name", None)
    return render_template("top.html",status="logout")

# home画面
@app.route('/')
@app.route('/index')
def home():
	if "user_name" in session:
		user_name = session["user_name"]
		not_joined_events = event_mapper.select_not_joined_event_overview(user_name)
		joined_events = event_mapper.select_joined_event_overview(user_name)
		my_events = event_mapper.select_my_event_overview(user_name)
		return render_template('index.html', not_joined_events = not_joined_events, joined_events = joined_events, my_events = my_events, name = user_name)
	else:
		return render_template('top.html')

@app.route('/add', methods=["POST"])
def add():
    if "user_name" in session:
        name = session["user_name"]
        event_name = request.form["event_name"]
        event_details = request.form["event_details"]
        date = request.form["date"]
        host = name
        event_mapper.insert_into_event_overview(event_name, event_details, date, host)
        return home()
    else:
        return render_template('top.html')

@app.route('/update', methods=['POST'])
def update():
    if "user_name" in session:
        event_id = request.form["event_id"]
        event_name = request.form["event_name"]
        event_details = request.form["event_details"]
        date = request.form["date"]
        host = session["user_name"]
        event_mapper.update_event_overview(event_id, event_name, event_details, date, host)
        return home()
    else:
        return render_template('top.html')

@app.route('/delete', methods=['POST'])
def delete():
    if "user_name" in session:
        event_id = request.form["event_id"]
        event_mapper.delete_event_overview(event_id)
        event_mapper.delete_event_attendees(event_id)
        return home()
    else:
        return render_template('top.html')

@app.route('/join_event', methods=['POST'])
def join_event():
    if "user_name" in session:
        event_id = request.form["event_id"]
        event_name = request.form["event_name"]
        user_name = session["user_name"]
        event_mapper.join_event(event_id, event_name, user_name)
        return home()
    else:
        return render_template('top.html')

@app.route('/exit_event', methods=['POST'])
def exit_event():
    if "user_name" in session:
        event_id = request.form["event_id"]
        user_name = session["user_name"]
        event_mapper.exit_event(event_id, user_name)
        return home()
    else:
        return render_template('top.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
