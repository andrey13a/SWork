# Classe usada para os serviços da aplicação
# Faz o acesso da entity ao repository

from entity.local_entity import Local


class LocalService:

    def __init__(self, repository):
        self.repository = repository

    def add_local(self, nome=str, responsavel=str):
        id = len(self.repository.get_all())
        local_obra = Local(id, nome, responsavel)
        self.repository.save(local_obra)
        return local_obra

    def get_locals(self):
        return self.repository.get_all()