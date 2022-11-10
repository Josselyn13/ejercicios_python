""" 9.1 Ejercicio 1 (2 puntos)
Realice un programa que pregunte aleatoriamente una multiplicación. El programa debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta). El programa preguntará 10 multiplicaciones, y al finalizar mostrará el número de aciertos. """

from random import randint, random

def prueba():
    print("Vamos a probarte en multiplicaciones: ")
    aciertos = 0
    for i in range(10):
        a = randint(2,9)
        b = randint(2,9)
        res = int(input(str(a) + " x " + str(b) + " = "))
        if (a*b==res):
            print("correcto")
            aciertos+=1
        else:
            print("incorrecto")
    print("El total de aciertos es: " + str(aciertos))            

if __name__ == '__main__':
    prueba()



""" 9.2 Ejercicio 2 (2 puntos)
Obtener el cuadrado de todos los elementos en la lista.
Lista: 1,2,3,4,5,6,7,8,9,10 """

def cuadrados():
    lista = [1,2,3,4,5,6,7,8,9,10]
    cuadrados = []
    for i in range(len(lista)):
        cuadrados.append(lista[i]**2)
    print(cuadrados)    

if __name__ == '__main__':
    cuadrados()

""" 9.3 Ejercicio 3 (2 puntos)
Obtener la cantidad de elementos mayores a 5 en la tupla.
tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3) """

total = 0
tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
print("Considerando la tupla: " + str(tupla))
for i in range(len(tupla)):
    if tupla[i]>5:
        total+=1
print("Existen " + str(total) + " números mayores a 5 en la tupla")        



