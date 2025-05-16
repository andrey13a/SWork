# base class for data persistence
import sqlite3
from entity.local_entity import Local


class LocalRepository:

    atributos = ["Id", "Nome", "Responsavel"]

    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""CREATE TABLE IF NOT EXISTS local_table(
                              id INTEGER PRIMARY KEY,
                              nome text,
                              responsavel text
                              )""")

    def save(self, local_obra):
        with self.conn:
            self.conn.execute("INSERT INTO local_table values(?,?,?)",(
                              local_obra.id,
                              local_obra.nome,
                              local_obra.responsavel))
    
    def get_all(self):
        with self.conn:
            return [Local(id, nome, responsavel) for id, nome, responsavel
                    in self.conn.execute("SELECT * FROM local_table")]
    