class Ordenacao:

    @staticmethod
    def Bolha(lista = []):

        """
        Método de Bolha
        :param lista
        :return lista
        """
        houveTroca = True
        while (houveTroca):
            houveTroca = False
            for i in range(0, len(lista)-1):
                if (lista[i] > lista[i+1]):
                    houveTroca = True
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
        return lista


    @staticmethod
    def Selecao(lista = []):

        """
        Método de Seleção
        :param lista
        :return lista
        """
        n = len(lista)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if lista[j] < lista[min_index]:
                    min_index = j
            lista[i], lista[min_index] = lista[min_index], lista[i]
        return lista


    @staticmethod
    def Insercao(lista=[]):

        """
        Método de Inserção
        :param lista
        :return lista
        """
        for i in range(1, len(lista)):
            aux = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > aux:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = aux
        return lista
