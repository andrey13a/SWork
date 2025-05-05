# Classe usada para permanencia das Ferramentas

class ToolRepository:

    def __init__(self):
        self.tools = []
        self.tipos = ["furadeira", "esmerilhadeira", "maquina de solda"]
        self.marcas = ["dewalt", "bosch", "arcweld"]
        self.atributos = ("id", "tipo", "tensao", "marca", "modelo", "condicao")

    
    def save(self, tool):
        self.tools.append(tool)
    
    def get_all(self):
        return self.tools
