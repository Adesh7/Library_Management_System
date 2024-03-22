import sqlite3
import os
from TypeOfEnums.PathEnum import Paths as pt
from TypeOfEnums.CredentialOperations import CredentialOperations as credOps
from string import Template
class insertInTable:
    cwd = os.chdir(pt.dbinstallPath.value)
    cwd = os.getcwd()
    print("Current Working Directory",cwd)
    db = sqlite3.connect("Library_Management_System.db")

    


    def __init__(self) -> None:
        pass

    def AddNewUser(self, userName, passWord):        
        with open(os.path.join(pt.insertPath.value,credOps.InsertCredentials),'r') as f:
            sql = f.read()
            query = Template(sql).substitute(UserName = userName,Password = passWord)
            try:
                cur = self.db.cursor()
                cur.execute(query)
            except:
                return False
            self.db.commit()
            self.db.close()
        
        return True
        
    def UpdatePassword(self,userName,passWord):
        with open(os.path.join(pt.updatePath.value,credOps.UpdateCredentials),'r') as f:
            sql = f.read()
            query = Template(sql).substitute(UserName = userName,Password = passWord)
            try:
                cur = self.db.cursor()
                cur.execute(query)
            except:
                return False
            self.db.commit()
            self.db.close()
        return True
        

