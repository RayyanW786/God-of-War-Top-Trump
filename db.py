import sqlite3
from typing import Union 

class DBUtils(object):
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cursor = self.conn.cursor()
    #    self.current_id = self.get_id()
    
    # def get_id(self) -> int:
    #     query = """
    #         SELECT UserID FROM USERDATA ORDER BY UserID desc LIMIT 1
    #     """
    #     self.cursor.execute(query)
    #     row = self.cursor.fetchall()
    #     if row == []:
    #         return 1
    #     else:
    #         return int(row[0][0])+1

    def create_user_table(self) -> None:
        query = """
            CREATE TABLE USERDATA
            (
                UserName TEXT,
                UserPwd TEXT,
                primary key (UserName)
            )
        """
        self.cursor.execute(query)
        self.conn.commit()
    
    def add_user(self, username: str, password: str) -> bool: #adds a user to the database
        if self.get_user(username) is not False:
            return False
        query = "INSERT INTO USERDATA VALUES  (?, ?)", [username, password]
        #self.current_id += 1
        self.cursor.execute(*query)
        self.conn.commit()
        return True
    
    def get_user(self, username: str) -> Union[bool, str]: #checks if a user is in the database and returns the pwd if they are else returns False
        query = "SELECT UserPwd FROM USERDATA WHERE UserName = ?", [username]
        self.cursor.execute(*query)
        row = self.cursor.fetchall()
        if row == []:
            return False
        else:
            return row[0][0]


    
    def exc(self, query: str) -> None:
        self.cursor.execute(query)
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()
