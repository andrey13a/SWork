# base class for locals


class Local:

    def __init__(self, id=str, nome=str, responsavel=str):
        self.id = id
        self.nome = nome
        self.responsavel = responsavel
    
    def __repr__(self):
        return f"id={self.id}, nome={self.nome}, responsavel={self.responsavel}"