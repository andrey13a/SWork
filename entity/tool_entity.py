# Classe base para todas as ferramentas

from datetime import datetime


class Tool:

    def __init__(self,
            id = str,
            tipo = str,
            tensao = str,
            marca = str,
            modelo = str,
            condicao = str,
            local = str):
        
        self.id = id
        self.tipo = tipo
        self.tensao = tensao
        self.marca = marca
        self.modelo = modelo
        self.condicao = condicao
        self.local = local

    def __repr__(self):
        return f"{self.id}, {self.tipo}, {self.tensao}, {self.marca}, {self.modelo}, {self.condicao}, {self.local}"