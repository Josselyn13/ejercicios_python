""" 5.1 Ejercicio 1 (2 puntos)
Programa que imprima si el número es positivo o negativo """

def signo():
    a = int(input("Introduzca un número: "))
    if a>0:
        print("El número es positivo")
    elif a<0:
        print("El número es negativo")
    else:
        print("El número es cero")        
if __name__ == '__main__':
    signo()

""" 5.2 Ejercicio 2 (2 puntos)
Programa que imprima si el número ingresado esta en el rango de 1 a 7 """

def rango():
    x = int(input("Introduzca un número: "))
    if 0<x and x<8:
        print("El número está entre 1 y 7")
    else:
        print("El número no está en el rango")


if __name__ == '__main__':
    rango()


""" 5.3 Ejercicio 3 (2 puntos)
Programa si el interés es mayor al 30%, sino informa el importe total: """

def descuento():
    cuentaTotal = 0
    cuenta = int(input("Ingrese el importe inicial: "))
    disc = int(input("Ingrese el porcentaje del descuento: "))
    if disc>30:
        cuentaTotal = cuenta*(1-(disc/100))
    else:
        print("No aplica descuento")
        cuentaTotal = cuenta
    print("Tu importe final es: "+ str(cuentaTotal))        


if __name__ == '__main__':
    descuento()




