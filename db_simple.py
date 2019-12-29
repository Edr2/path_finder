import psycopg2
from app import db_conf

conn = psycopg2.connect(user=db_conf['user'], password=db_conf["password"], host=db_conf["host"], port=db_conf["port"],
                        database=db_conf["db"])
cursor = conn.cursor()
