class Aluno:
    def __init__(self, nome, idade):

        """
        Construtor
        :param nome
        :param idade
        """
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def __str__(self):
        """
        :return nome e idade em formato de String
        """
        return f"Aluno [ nome={self.nome}, idade={self.idade} ]"

    def __lt__(self, other):
        """
        Implementa comparação para ordenar por nome e, em caso de empate, por idade.
        :return nome, idade
        """
        if self.nome == other.nome:
            return self.idade < other.idade
        return self.nome < other.nome
