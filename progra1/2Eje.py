def validarNumero(numero):
    if numero < 1:
        return True
    return False

def validarMes(mes):
    if mes > 12:
        return True
    return False

def esBisiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False


def validarDia(dia,mes,año):
    if mes == 2:
        if(esBisiesto(año)):
            if dia > 29:
                return True
        else:
            if dia > 28:
                return True
    elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
        return True
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11 ) and dia > 30:
        return True
    return False

dia = int(input("Ingrese el dia: "))

mes = int(input("Ingrese el mes: "))

año = int(input("Ingrese el año: "))


if not ((validarNumero(dia) or validarNumero(año) or validarNumero(mes))):
    if not(validarDia(dia,mes,año) or validarMes(mes)):
        print("La fecha es valida")
    else:
        print("La fecha es invalida")
else:
    print("La fecha no pueden tener numeros negativos")
