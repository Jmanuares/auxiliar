lista = [1,2,3,4,5,6,7,8,9,10,11,12,6]
def ejercicio1():
    #Verifica la cantidad de veces que aparece un numero dado en una lista ya cargada
    numero = int(input("ingrese un numero: "))

    ocurrencias = 0
    for item in lista:
        if item == numero:
            ocurrencias += 1

    print(ocurrencias)

def ejercicio2():
    #un programa que intercambie el primer y ultimo elemento de una lista precargada
    aux = lista[0]
    lista[0] = lista[len(lista)-1]
    lista[len(lista)-1] = aux

def ejercicio3():
    #nada
    return

def ejercicio4():
    #nada
    return
