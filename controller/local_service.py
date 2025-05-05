# Classe usada para os serviços da aplicação
# Faz o acesso da entity ao repository

from entity.local_entity import Local


class LocalService:

    def __init__(self, repository):

        self.repository = repository
    

    def add_local(self, nome=str, responsavel=str):

        local = Local(nome, responsavel)
        self.repository.save(local)
        return local

    def get_locals(self):
        return self.repository.get_all()