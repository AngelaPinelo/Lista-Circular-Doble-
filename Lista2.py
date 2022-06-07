class Nodo:
    def __init__(self,valor_):
        self.valor = valor_
        self.siguiente=None
        self.anterior=None

class ListaCircular:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    #Este método inserta al inicio pero no es del todo doble circular
    '''def insertar2(self,valor_):
        nuevo=Nodo(valor_)
        if (self.primero==None):
            self.primero=nuevo
        else:
            nuevo.siguiente=self.primero
            self.primero.anterior=nuevo
            self.primero=nuevo
            self.primero.anterior=self.ultimo'''

    def insertaralfinal(self,valor_):
        nuevo=Nodo(valor_)
        if (self.primero==None):
            self.primero=self.ultimo=nuevo
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nuevo
            self.ultimo.anterior = aux
            self.ultimo.siguiente=self.primero
            self.primero.anterior=self.ultimo

    def imprimir(self):
        print("Elementos de la lista circular doblemente enlazada:")
        print('----------------------------------------------------')
        aux=self.primero
        while(aux!=None):
            print(aux.valor)
            if (aux.siguiente==self.primero):
                return
            aux=aux.siguiente

    def buscar(self, valor_buscado):
        aux=self.primero
        while(aux!=None):
            if (aux.valor==valor_buscado):
                print("actual: ",aux.valor)
                print("siguiente: ",aux.siguiente.valor)
                print('anterior: ',aux.anterior.valor)

            if (aux.siguiente==self.primero):
                return
            aux=aux.siguiente

    def primeros(self):
        aux=self.primero
        print('Este es el primer número en la lista:')
        print(aux.valor)

lista = ListaCircular()
lista.insertaralfinal(10)
lista.insertaralfinal(48)
lista.insertaralfinal(74)
lista.insertaralfinal(25)
lista.insertaralfinal(38)
lista.primeros()

lista.imprimir()

op=input("Selecciona un número de la lista:")
ok=int(op)
print(lista.buscar(ok))