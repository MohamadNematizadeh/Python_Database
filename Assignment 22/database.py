from datetime import datetime
import sqlite3
class Database:
    def __init__(self):
        self.con = sqlite3.connect("todo_list.db")
        self.cursor = self.con.cursor()

    def get_tasks (self):
        query = "SELECT * FROM tasks"
        result= self.cursor.execute(query)    
        tasks = result.fetchall()
        return tasks
    def add_new_task(self,new_title,new_description,new_time,new_date):
        try:
            query = f"INSERT INTO tasks(title,description,time,date) VALUES ('{new_title}','{new_description}',{new_time},{new_date})"
            self.cursor.execute(query)
            self.con.commit()
            return True  
        except:
            return False   
    def delet_tasks (self,id):
            self.cursor.execute(f"DELETE FROM tasks WHERE id = {id}")
            self.con.commit()
            return True
    
    def task_done(self,id):
        self.cursor.execute(f"SELECT * FROM tasks WHERE id ='{id}'")
        task = self.cursor.fetchone()
        if task !=  None:
            self.cursor.execute(f"UPDATE tasks SET is_done ='1' WHERE id ='{id}'")
            self.con.commit()

