from datetime import datetime
import sqlite3
class Database():
    def __init__(self):
        self.con = sqlite3.connect("1/todo_list.db")
        self.cursor = self.con.cursor()
        self.tasks= []

    def get_alarms(self):
        query = "SELECT * FROM tasks"
        result=self.cursor.execute(query)    
        tasks = result.fetchall()
        return tasks

    def add_new_alarm(self,edit_id,edit_title,edit_time):
        print(1)
        try:
            print(2)
            query = f"INSERT INTO alarms SET id={edit_id}(title,time)VALUES('{edit_title}','{edit_time}')"
            self.cursor.execute(query)
            self.con.commit()
            return True
            print(1)
        
        except:
            return False
            print(2)

    def remove_task(self,id):
        try:
            self.cursor.execute(f"DELETE FROM alarms WHERE id = '{id}'")
            self.con.commit()
            return True

        except:
            return False

    def edit_alarm(self,neme,time):
         try:
             self.cursor.execute(f"UPDATE alarms(name,time)VALUES('{new_name}','{new_time}'")   
             self.con.commit()
             return True
         except:
             return False     