# LKL-Bot\bot\db_mysql.py
import pymysql, contextlib, config

@contextlib.contextmanager
def get_mysql():
    conn = pymysql.connect(host=config.MYSQL_HOST,
                         user=config.MYSQL_USER,
                         password=config.MYSQL_PASS,
                         database=config.MYSQL_DB,
                         autocommit=True)
    try:
        yield conn
    finally:
        conn.close()