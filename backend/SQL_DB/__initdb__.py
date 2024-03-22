import sqlite3
import os,glob
from TypeOfEnums.PathEnum import Paths as pt

class Library_Management_System_DB:
  def __init__(self) -> None:
     pass
     
  def db_Creation(self):
    print(pt.dbinstallPath.value)
    cwd = os.getcwd()
    print(cwd)
    os.chdir(pt.dbinstallPath.value)
    cwd = os.getcwd()
    print("cwd:", cwd)
    db = sqlite3.connect('Library_Management_System.db')

    for filename in glob.glob(os.path.join(pt.schemaPath.value,'*.sql')):
        print("Executing File",filename)
        with open(os.path.join(os.getcwd(), filename),'r') as f:
            db.executescript(f.read())
            db.commit()
    
    db.close()

""" cur = db.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            ) """

    



     
