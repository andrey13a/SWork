# Classe usada para os serviços da aplicação
# Faz o acesso da entity ao repository

from entity.tool_entity import Tool


class ToolService:

    def __init__(self, repository):
        self.repository = repository
    
    def add_tool(self, id=str, tipo = str, tensao = str, marca = str, modelo = str, condicao = str, local = str):
        tool = Tool(id, tipo, tensao, marca, modelo, condicao, local)
        self.repository.save(tool)
        return tool
    
    def get_tools(self):
        return self.repository.get_all()
    