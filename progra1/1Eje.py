def comparar(numero1, numero2, numero3):
#recibe 3 numeros positivos y devuelve el mayor estricto
#si no existe devuelve -1
    numeroFinal = 0
    if numeroFinal < numero1:
        numeroFinal = numero1
    if numeroFinal <= numero2:
        if numeroFinal == numero2:
            return -1
        numeroFinal = numero2
    if numeroFinal <= numero3:
        if numeroFinal == numero3:
            return -1
        numeroFinal = numero3


    return numeroFinal

def validarNumero(numero):
    if numero < 1:
        return True
    return False

numero1 = int(input("Ingrese el primer numero: "))
while(validarNumero(numero1)):
    numero1 = int(input("Numero invalido un numero positivo: "))
    
numero2 = int(input("Ingrese el segundo numero: "))
while(validarNumero(numero2)):
    numero2 = int(input("Numero invalido un numero positivo: "))

numero3 = int(input("Ingrese el tercer numero: "))
while(validarNumero(numero3)):
    numero3 = int(input("Numero invalido un numero positivo: "))

mayor = comparar(numero1, numero2, numero3)
if mayor == -1:
    print("Existen numeros repetidos")
else:
    print("El numero mayor ingresado fue", mayor)