class Database:

    def create_table_bucket(self):
        sql = """
        CREATE TABLE Bucket(
        user_id INT NOT NULL,
        bucket TEXT,
        PRIMARY KEY (user_id)
        );
        """
        self.execute(sql, commit=True)

    def select_users_bucket(self, user_id: int) -> str:
        sql = 'SELECT * FROM Bucket WHERE user_id = ?'
        return self.execute(sql, parametrs=(user_id,), commit=True)

    def add_item_to_bucket(self, user_id: int, item_id: int):
        items = self.select_users_bucket(user_id)
        items += f'{items} {item_id}'
        sql = 'UPDATE Bucket SET item_id = ? WHERE user_id = ?'
        self.execute(sql, parametrs=(items, user_id), commit=True)