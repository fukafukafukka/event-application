import MySQLdb
import connection_password_mysqldb
import logging.config
import datetime

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
            charset="utf8",
            use_unicode=True)
    return con

def insert_into_event_overview(event_name, event_details, date, host):
    con = None
    try:
        con = get_con()
    except Exception as e:
        logger.log(30,'MySQLとの接続エラー発生')
        raise(e)

    # カーソルを取得する
    cur= con.cursor()

    try:
        tdatetime = datetime.datetime.strptime(date, '%Y-%m-%d')
        tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
        # 車体をinsertする
        cur.execute(
            "INSERT INTO event_overview(event_name, event_details, date, host) \
            VALUES (%s,%s,%s,%s)", \
            (event_name, event_details, tdate, host))
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Insert処理失敗')
        raise(e)

def select_joined_event_overview(user_name):
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
            "SELECT a.event_id, a.event_name, a.event_details, a.date \
                FROM event_overview AS a \
                WHERE EXISTS ( \
                    SELECT * FROM event_attendees AS b \
                        WHERE b.attendees = '%s' \
                            and b.event_id = a.event_id \
                );" % user_name)
        joined_events = cur.fetchall()
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Select処理失敗(select_all_event_overview)')
        raise(e)

    return joined_events

def select_not_joined_event_overview(user_name):
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
            "SELECT a.event_id, a.event_name, a.event_details, a.date\
                FROM event_overview AS a \
                LEFT JOIN event_attendees AS b \
                    ON b.attendees = '%s' \
                       AND b.event_id = a.event_id \
                WHERE b.attendees IS NULL;" % user_name)
        not_joined_events = cur.fetchall()
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Select処理失敗(select_all_event_overview)')
        raise(e)

    return not_joined_events

def select_my_event_overview(user_name):
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
            "SELECT * FROM event_overview where host = '%s'" % user_name)
        my_events = cur.fetchall()
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Select処理失敗(select_my_event_overviewメソッド)')
        raise(e)

    return my_events

def update_event_overview(event_id, event_name, event_details, date, host):
    con = None
    try:
        con = get_con()
    except Exception as e:
        logger.log(30,'MySQLとの接続エラー発生')
        raise(e)

    # カーソルを取得する
    cur= con.cursor()

    try:
        tdatetime = datetime.datetime.strptime(date, '%Y-%m-%d')
        tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)

        sql = "UPDATE event_overview SET event_name = %s, event_details = %s, date = %s, host = %s WHERE event_id = %s"
        cur.execute(sql, (event_name, event_details, tdate, host, event_id))
        r = cur.fetchall()

        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Update処理失敗')
        raise(e)

def delete_event_overview(event_id):
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
            "DELETE FROM event_overview WHERE event_id = '%s'" % event_id
        )
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Delete処理失敗')
        raise(e)

def delete_event_attendees(event_id):
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
            "DELETE FROM event_attendees WHERE event_id = '%s'" % event_id
        )
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Delete処理失敗')
        raise(e)

def join_event(event_id, event_name, user_name):
    con = None
    try:
        con = get_con()
    except Exception as e:
        logger.log(30,'MySQLとの接続エラー発生')
        raise(e)

    # カーソルを取得する
    cur= con.cursor()

    try:
        # 車体をinsertする
        cur.execute(
            "INSERT INTO event_attendees(event_id, event_name, attendees) \
            VALUES (%s,%s,%s)", \
            (event_id, event_name, user_name))
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Delete処理失敗')
        raise(e)

def exit_event(event_id, user_name):
    con = None
    try:
        con = get_con()
    except Exception as e:
        logger.log(30,'MySQLとの接続エラー発生')
        raise(e)

    # カーソルを取得する
    cur= con.cursor()

    try:
        print(event_id)
        print(user_name)
        cur.execute(
            "DELETE FROM event_attendees WHERE event_id = '%s' AND attendees = '%s';" % (int(event_id), user_name))
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Delete処理失敗')
        raise(e)