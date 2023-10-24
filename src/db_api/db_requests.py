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
        connection.close()
        return data

    def create_table_items(self):
        sql = """
        CREATE TABLE Items(
        id INT NOT NULL,
        name TEXT,
        amount INT,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_item(self, id: int, name: str = None, amount: int = 0):
        sql = 'INSERT INTO Items(id, name, amount) VALUES(?, ?, ?)'
        parameters = (id, name, amount)
        self.execute(sql, parameters, commit=True)

    def select_item_info(self, **kwargs) -> list:
        sql = 'SELECT * FROM Items WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def select_all_items(self) -> list:
        sql = 'SELECT * FROM Items'
        return self.execute(sql, fetchall=True)

    def update_item_name(self, id: int, name: str):
        sql = 'UPDATE Items SET name = ? WHERE id = ?'
        return self.execute(sql, parametrs=(name, id), commit=True)

    def update_item_amount(self, id: int, amount: int):
        sql = 'UPDATE Items SET amount = ? WHERE id = ?'
        return self.execute(sql, parametrs=(amount, id), commit=True)

    def delete_item(self, **kwargs):
        sql = 'DELETE FROM Items WHERE '
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parametrs=parameters, commit=True)

    def delete_all(self):
        self.execute('DELETE FROM Items WHERE True', commit=True)

    def drop_all(self):
        self.execute('DROP TABLE Items', commit=True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += ' AND '.join([f'{item} = ?' for item in parameters])
        return sql, tuple(parameters.values())
