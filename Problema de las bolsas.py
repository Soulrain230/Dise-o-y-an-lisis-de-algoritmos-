def algoritmo(lista, capacidad):
    bolsas = []
    while lista:
        bolsa = []   # crea una nueva bolsa
        aux = capacidad
        for i in lista[:]:  # se hace una copia de la lista
            if aux - i >= 0:
                aux -= i
                bolsa.append(i)
                lista.remove(i)  # elimina el objeto de la lista original
        bolsas.append(bolsa)# añade la bolsa a la lista de bolsas    
    return len(bolsas), bolsas

def star():
    lista_Objetos = [6, 5, 3, 4, 3, 5, 3, 3, 3, 2, 2, 1, 1, 1, 1]

    num_bolsas, contenido_bolsas = algoritmo(lista_Objetos, 7)

    print("numero de bolsas utilizadas:", num_bolsas)
    
    for i in range(num_bolsas): 
         print("bolsa",i+1,": ", contenido_bolsas[i])

star()