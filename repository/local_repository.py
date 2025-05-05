# base class for data persistence


class LocalRepository:

    def __init__(self):
        self.locals = []
    
    def save(self, local):
        self.locals.append(local)
    
    def get_all(self):
        return self.locals