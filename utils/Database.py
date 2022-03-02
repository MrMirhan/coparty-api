import mysql.connector as mysql
import sys
sys.path.append("../..")
import config

dbparty = mysql.connect(
  host=config.MYSQL_HOST,
  user=config.MYSQL_USER,
  password=config.MYSQL_PASSWORD,
  database=config.MYSQL_DATABASE
)