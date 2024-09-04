import random

from Aluno import Aluno

class Util:

    @staticmethod
    def gerador(tamanho):

        """
        Método que randomiza o nome e idade dos alunos

        :param tamanho
        :return nome e idade
        """
        letras = 'abcdefghijklmnopqrstuvwxyz'
        nomes = ''

        for i in range(tamanho):
            letra_sorteada = letras[random.randint(0, len(letras) - 1)]
            nomes += letra_sorteada

        idade = random.randint(18, 70)
        return nomes, idade

    @staticmethod
    def geradorParaLista(lista, quantidade, tamanho):

        """
        Método para popular a lista com nome e idade dos alunos

        :param lista
        :param quantidade
        :param tamanho
        """
        for i in range(quantidade):
            nome, idade = Util.gerador(tamanho)
            lista.append(Util.gerador(tamanho))
