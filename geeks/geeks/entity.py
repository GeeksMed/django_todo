class ToDo:
    def __init__(self, id, assunto, descricao, prioridade, data_limite):
        self.__id = id
        self.__assunto = assunto
        self.__descricao = descricao
        self.__prioridade = prioridade
        self.__data_limite = data_limite

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def assunto(self):
        return self.__assunto

    @assunto.setter
    def assunto(self, assunto):
        self.__assunto = assunto

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def prioridade(self):
        return self.__prioridade

    @prioridade.setter
    def prioridade(self, prioridade):
        self.__prioridade = prioridade

    @property
    def data_limite(self):
        return self.__data_limite

    @data_limite.setter
    def data_limite(self, data_limite):
        self.__data_limite = data_limite

    def __repr__(self):
        return f'{self.id}, {self.assunto}, {self.descricao}, {self.prioridade}, {self.data_limite}'
