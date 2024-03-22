import os
from enum import Enum
class Paths(Enum):
    currentWorkingDirectory = os.getcwd()
    dbinstallPath = currentWorkingDirectory+ "\\backend\\SQL_DB"
    schemaPath = currentWorkingDirectory +"\\backend\\SQL_DB\\DB_SCHEMA"
    insertPath = currentWorkingDirectory + "\\backend\\SQL_DB\\INSERT_SCRIPTS"
    updatePath = currentWorkingDirectory + "backend\SQL_DB\UPDATE_SCRIPTS"
    
    def __str__(self):
        return str(self.value)