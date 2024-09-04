from Util import Util
from Ordenacao import Ordenacao

    """
    Main Class para execução do código
    """
import random

lista_bolha = []
lista_insercao = []
lista_selecao = []
lista_sort = []

quantidade = 60000

tamanhoNome = random.randint(3, 6)

Util.geradorParaLista(lista_sort, quantidade, tamanhoNome)
Util.geradorParaLista(lista_bolha, quantidade, tamanhoNome)
Util.geradorParaLista(lista_selecao, quantidade, tamanhoNome)
Util.geradorParaLista(lista_insercao, quantidade, tamanhoNome)

print("\\n Lista com método sort \\n")
lista_sort = sorted(lista_sort)
for aluno in lista_sort:
    print(aluno)
    
print("\\n Lista com método bolha \\n")
Ordenacao.Bolha(lista_bolha)
for aluno in lista_bolha:
    print(aluno)
    
print("\\n Lista com método seleção \\n")
Ordenacao.Selecao(lista_selecao)
for aluno in lista_selecao:
    print(aluno)

print("\n Lista com método inserção \n")
Ordenacao.Insercao(lista_insercao)
for aluno in lista_insercao:
    print(aluno)
