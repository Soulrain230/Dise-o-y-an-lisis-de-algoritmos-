def busqueda_binaria(lista, elemento):
    if len(lista) > 0:
        aux = lista[len(lista)//2]
        if aux > elemento:
            return busqueda_binaria(lista[:len(lista)//2], elemento)
        elif aux < elemento:
            return busqueda_binaria(lista[len(lista)//2+1:], elemento)
        else:
            return "Esta en la lista"
    else:
            return "No esta en la lista"

def main():
    
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    

    print(lista)    
    print(busqueda_binaria(lista, 9)) 



main()