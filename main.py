import sqlite3
from dotenv import load_dotenv
from os import getenv
from sys import argv

load_dotenv()

class Database:
  def __init__(self, db_name):
    self.connection = sqlite3.connect(db_name)
    self.cursor = self.connection.cursor()

  def __del__(self):
    self.connection.close()

  def create_table(self, sql: str):
    self.cursor.execute(sql)
    self.connection.commit()
  
  def insert(self, table, *values):
    self.cursor.execute(f"INSERT INTO {table} VALUES ({','.join(['?' for _ in values])})", values)
    self.connection.commit()


if len(argv) > 1 and argv[1] == 'db-setup':
  print('Creating table in database...')
  db = Database(getenv('DB_NAME'))
  db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')


if len(argv) > 1 and argv[1] == 'insert':
  print('Adding new url address...')
  category = argv[2]
  url = argv[3]
  db = Database(getenv('DB_NAME'))
  db.insert('urls', None, category, url)