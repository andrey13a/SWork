# Classe usada para permanencia das Ferramentas
import sqlite3
from entity.tool_entity import Tool

class ToolRepository:

    atributos = ["Id", "Tipo", "Tensao", "Marca", "Modelo", "Condicao"]

    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""CREATE TABLE IF NOT EXISTS tools_table(
                             id INTEGER PRIMARY KEY,
                             tipo text,
                             tensao text,
                             marca text,
                             modelo text,
                             condicao text
                             )"""
                              )

    def save(self, tool):
        with self.conn:
            self.conn.execute("INSERT INTO tools_table values(?,?,?,?,?,?)",(
                                tool.id, 
                                tool.tipo, 
                                tool.tensao, 
                                tool.marca, 
                                tool.modelo, 
                                tool.condicao
                               )
                               )

    def get_all(self):
        with self.conn:
            return [Tool(id, tipo, tensao, marca, modelo, condicao) for id, tipo, tensao, marca, modelo, condicao 
                    in self.conn.cursor().execute("SELECT * FROM tools_table")]
