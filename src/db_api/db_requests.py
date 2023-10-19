import sqlite3


class Database:
    def __init__(self, path_db: str = 'shop_database.db'):
        self.path_db = path_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_db)


    def execute(self, sql, parametrs: tuple = tuple(), fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parametrs)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        return data
