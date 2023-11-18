import random

def numero_desconocido():
    numero_aleatorio = random.randint(1, 9999) #estableco el rango del numero a buscar
    tamanio = str(numero_aleatorio)

    if len(tamanio) == 1:               #agrego 0 para rellenar los espcaios faltantes
        tamanio="000"+tamanio
        return tamanio
    elif len(tamanio) == 2:
        tamanio="00"+tamanio
        return tamanio
    elif len(tamanio) == 3:
        tamanio="0"+tamanio
        return tamanio
    else:
        return tamanio



def numero_Descompuesto():              #separo los digitos del numero
    numero = numero_desconocido()
    descompuesto = []
    for i in numero:
        descompuesto.append(i)
    return descompuesto


def comparacion(original, usuario):     #se hace la comparacion entre las 2 varianbles
    correctos = []
    incorrectos = []

    for i in range(len(original)):
        if original[i] == usuario[i]:
            correctos.append(original[i])
        elif usuario[i] in original:
            correctos.append("[ ]")
            incorrectos.append(usuario[i])

    return  correctos, incorrectos


def juego():
    numero = numero_Descompuesto()
    print(numero)
    print("[ ],[ ],[ ],[ ]")
    while True:
        intento = list(input("Ingrese un número de 4 cifras, por ejemplo: 0003\n"))
        ok, no = comparacion(numero, intento)
        if intento == numero:
            print("¡Felicidades! has adivinado el número.")
            break
        else:
            print("Los siguientes numeros estan en su posicion correcta")
            print(ok)
            if len(no) >0:
             print("Los números: " + ', '.join(map(str, no)) + " estan en el numero pero no están en la posición correcta")
            print("Inténtalo de nuevo.")
juego()