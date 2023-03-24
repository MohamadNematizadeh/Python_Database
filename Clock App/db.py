import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect('alarm_list.db')
        self.cursor = self.con.cursor()

    def get_alarms(self):
        query = 'SELECT * FROM alarms'
        result = self.cursor.execute(query)
        alarms = result = result.fetchall()
        return alarms

    def add_new_alarm(self, time):
        try:
            query = f'INSERT INTO alarms(time) VALUES("{time}")'
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def remove_alarm(self,id):
        try:
            query = f'DELETE FROM alarms WHERE id = "{id}"'
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def edit_alarm(self, second, id):
        try:
            query = f'UPDATE alarms SET time="{second}" WHERE id = {id}'
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
