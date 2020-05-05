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
            charset="utf8",
            use_unicode=True)
    return con

def insert_into_tank_bodies(tank_name, be_shot_count, engine, fuel_tank, gun, caterpillar):
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
            "INSERT INTO tank_bodies(tank_name, be_shot_count, engine_name, fuel_tank_name, gun_name, caterpillar_name) \
            VALUES (%s,%s,%s,%s,%s,%s)", \
            (tank_name, be_shot_count, engine.name, fuel_tank.name, gun.name, caterpillar.name))

        # 戦車IDを取得する
        cur.execute(
            "SELECT tank_id FROM tank_bodies ORDER BY tank_id DESC LIMIT 1"
        )
        latest_tank_id = cur.fetchone()

        # キャタピラをinsertする
        cur.execute(
            "INSERT INTO caterpillar(tank_id, caterpillar_name) \
            VALUES (%s,%s)", \
            (latest_tank_id, caterpillar.name))

        # エンジンをinsertする
        cur.execute(
            "INSERT INTO engine(tank_id, engine_name) \
            VALUES (%s,%s)", \
            (latest_tank_id, engine.name))

        # 燃料タンクをinsertする
        cur.execute(
            "INSERT INTO fuel_tank(tank_id, fuel_tank_name, fuel) \
            VALUES (%s,%s,%s)", \
            (latest_tank_id, fuel_tank.name, fuel_tank.fuel))

        # 砲塔をinsertする
        cur.execute(
            "INSERT INTO gun(tank_id, gun_name) \
            VALUES (%s,%s)", \
            (latest_tank_id, gun.name))

        # 砲塔IDを取得する
        cur.execute(
            "SELECT gun_id FROM gun ORDER BY gun_id DESC LIMIT 1"
        )
        latest_gun_id = cur.fetchone()

        # shellをinsertする
        for shell in gun.shell_cover:
            cur.execute(
            "INSERT INTO shell(gun_id, shell_name, shell_class) \
            VALUES (%s,%s,%s)", \
            (latest_gun_id, shell.name, shell.SHELL_CLASS_NAME))
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Insert処理失敗')
        raise(e)

def select_event_overview():
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
            "SELECT * FROM event_overview")
        all_events = cur.fetchone()
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Select処理失敗')
        raise(e)

    return all_events

def update_tank(tank_id, tank_name, engine_name, fuel_tank_name, gun_name, caterpillar_name):
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
        sql = "UPDATE tank_bodies SET tank_name = %s WHERE tank_id = %s"
        cur.execute(sql, (tank_name, tank_id))
        r = cur.fetchall()
        con.commit()

        sql = "UPDATE tank_bodies SET gun_name = %s WHERE tank_id = %s"
        cur.execute(sql, (gun_name, tank_id))
        r = cur.fetchall()
        con.commit()

        sql = "UPDATE tank_bodies SET engine_name = %s WHERE tank_id = %s"
        cur.execute(sql, (engine_name, tank_id))
        r = cur.fetchall()
        con.commit()

        sql = "UPDATE tank_bodies SET fuel_tank_name = %s WHERE tank_id = %s"
        cur.execute(sql, (fuel_tank_name, tank_id))
        r = cur.fetchall()
        con.commit()

        sql = "UPDATE tank_bodies SET caterpillar_name = %s WHERE tank_id = %s"
        cur.execute(sql, (caterpillar_name, tank_id))
        r = cur.fetchall()
        con.commit()

        # Gunテーブルをアップデートする。
        sql = "UPDATE gun SET gun_name = %s WHERE tank_id = %s"
        cur.execute(sql, (gun_name, tank_id))
        r = cur.fetchall()
        con.commit()

        # fuel_tankテーブルをアップデートする。
        sql = "UPDATE fuel_tank SET fuel_tank_name = %s WHERE tank_id = %s"
        cur.execute(sql, (fuel_tank_name, tank_id))
        r = cur.fetchall()
        con.commit()

        # engineテーブルをアップデートする。
        sql = "UPDATE engine SET engine_name = %s WHERE tank_id = %s"
        cur.execute(sql, (engine_name, tank_id))
        r = cur.fetchall()
        con.commit()

        # caterpillarテーブルをアップデートする。
        sql = "UPDATE caterpillar SET caterpillar_name = %s WHERE tank_id = %s"
        cur.execute(sql, (caterpillar_name, tank_id))
        r = cur.fetchall()

        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Select処理失敗')
        raise(e)


def delete_tank(tank_id):
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
            "DELETE FROM tank_bodies WHERE tank_id = '%s'" % tank_id
        )

        # 砲弾テーブルから削除する。
        cur.execute("SELECT gun_id FROM gun WHERE tank_id = '%s'" % tank_id)
        gun_id = cur.fetchone()
        cur.execute("SELECT shell_name FROM shell WHERE gun_id = '%s'" % gun_id)
        shell_name = cur.fetchone()
        if shell_name != None:
            cur.execute(
                "DELETE FROM shell WHERE gun_id = '%s'" % gun_id
            )

        # Gunテーブルから削除する。
        cur.execute(
            "DELETE FROM gun WHERE tank_id = '%s'" % tank_id
        )

        # エンジンテーブルから削除する。
        cur.execute(
            "DELETE FROM engine WHERE tank_id = '%s'" % tank_id
        )

        # 燃料タンクテーブルから削除する。
        cur.execute(
            "DELETE FROM fuel_tank WHERE tank_id = '%s'" % tank_id
        )

        # キャタピラテーブルから削除する。
        cur.execute(
            "DELETE FROM caterpillar WHERE tank_id = '%s'" % tank_id
        )

        # cur.fetchall()
        con.commit()
        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Select処理失敗')
        raise(e)

def get_all_tanks():
    con = None
    try:
        con = get_con()
    except Exception as e:
        logger.log(30,'MySQLとの接続エラー発生')
        raise(e)

    # カーソルを取得する
    cur= con.cursor()

    tanks = None

    try:
        # クエリを実行する
        sql = "SELECT * FROM tank_bodies"
        cur.execute(sql)

        # 実行結果をすべて取得する
        tanks = cur.fetchall()

        # 一行ずつ表示する
        if len(tanks) != 0:
            for tank in tanks:
                print(tank)

        cur.close()
        con.close()
    except Exception as e:
        logger.log(30,'MySQL、Select処理失敗')
        raise(e)

    return tanks