import MySQLdb
import connection_password_mysqldb
import logging.config

# ログ設定ファイルからログ設定を読み込み
logging.config.fileConfig('/app/src/log/log.conf')
logger = logging.getLogger()

def get_con():
    """ 接続サンプル """

    # 接続する
    con = MySQLdb.connect(
            user=connection_password_mysqldb.user,
            passwd=connection_password_mysqldb.passwd,
            host=connection_password_mysqldb.host,
            db=connection_password_mysqldb.db,
            charset="utf8")
    return con

def select_user(user_name):
    print("user_name:"+user_name)
    con = None
    try:
        con = get_con()
    except Exception as e:
        logger.log(30,'MySQLとの接続エラー発生')
        raise(e)

    # カーソルを取得する
    cur= con.cursor()

    user = None

    try:
        cur.execute(
            "SELECT * FROM users WHERE user_name = '%s'" % user_name)
        user = cur.fetchone()

        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Select処理失敗')
        raise(e)

    return user

def insert_user(user_name, password):
    con = None
    try:
        con = get_con()
    except Exception as e:
        logger.log(30,'MySQLとの接続エラー発生')
        raise(e)

    # カーソルを取得する
    cur= con.cursor()

    try:
        cur.execute(
            "INSERT INTO users(user_name, password) \
            VALUES (%s,%s)", \
            (user_name, password))
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Insert処理失敗')
        raise(e)
    return user_name, password

def update_password(user_name, password):
    con = None
    try:
        con = get_con()
    except Exception as e:
        logger.log(30,'MySQLとの接続エラー発生')
        raise(e)

    # カーソルを取得する
    cur= con.cursor()

    try:
        # 車体テーブルをアップデートする。
        sql = "UPDATE users SET password = %s WHERE user_name = %s"
        cur.execute(sql, ({password}, {user_name}))
        r = cur.fetchall()
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Insert処理失敗')
        raise(e)
    return user_name, password


def delete_user(user_name, password):
    con = None
    try:
        con = get_con()
    except Exception as e:
        logger.log(30,'MySQLとの接続エラー発生')
        raise(e)

    # カーソルを取得する
    cur= con.cursor()

    try:
        # 車体テーブルから削除する。
        cur.execute(
            "DELETE FROM users WHERE user_name = '%s' and password = '%s'" % user_name, password
        )

        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Select処理失敗')
        raise(e)
