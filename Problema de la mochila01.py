class Objeto:
    def __init__(self, nombre, beneficio, peso): # creamos objeto con nombre, peso y beneficio
        self.nombre = nombre
        self.beneficio = beneficio
        self.peso = peso

def mochila(capacidad, objetos): #algoritmo para agregar los objeos a la mochila
    dentro_Mochila = []
    puntero = capacidad
    for objeto in objetos: #repeticiones es igual a la cantidad de entidades de tipio "objetos" hay dentro de la lista objetos
        if objeto.peso <= puntero:
            dentro_Mochila.append(objeto)
            puntero -= objeto.peso
        elif puntero <= 0:# solo rompe si puntero ya esta en 0
            break
    return dentro_Mochila


def star():
    lista_objetos = [Objeto("pesa",5,1), Objeto("balon",3,4), Objeto("botella",1,1), Objeto("sombrero",2,1)]#crea la lista de objetos
    lista_objetos.sort(key=lambda objeto: objeto.beneficio, reverse= True)#orddena la lista por beneficio de mayor a menor puede cambiarse por otro metodo de ordenamiento
    print("Lista de objetos:")
    for objeto in lista_objetos:
        print(" nombre: ", objeto.nombre, " beneficio: ",objeto.beneficio, " peso: ", objeto.peso) #imprime la lista de ojetos
    
    obje_Mochila=mochila(3,lista_objetos)#llamo al algoritmo mochila

    print("\n"+ "\n")
    print("objetos en la mochila")
    for objeto in obje_Mochila:
        print(" nombre: ", objeto.nombre, " beneficio: ",objeto.beneficio, " peso: ", objeto.peso)#imprime la lista de ojetos que estan en la mochila

star() #inicia