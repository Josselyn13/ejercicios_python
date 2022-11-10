""" 4.1 Ejercicio 1(1.2 puntos)
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo. """
import random
def run():
    lista = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        lista[i] = random.randint(1,10)
        print("El elemento " + str(i) + " de la lista es: " + str(lista[i]) + " Su cuadrado es: " + str(lista[i]**2) + " y su cubo es: " + str(lista[i]**3))

if __name__ == '__main__':
    run()


""" 4.2 Ejercicio 2 (1.2 puntos)
Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla. """

def ejercicio42():
    lista2 = ["","","","",""]
    for i in range(5):
        lista2[i] = input("Ingrese el elemento " + str(i) + " de la lista: ")
    print(lista2[::-1])    
    
if __name__ == '__main__':
    ejercicio42()


""" 4.3 Ejercicio 3 (1.2 puntos)
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor. """

def calificaciones():
    calif = []
    mayor = 0
    suma = 0
    for i in range(5):
        a=int(input('Ingrese calificación entre 0 y 10\n'))
        suma += a
        calif.append(a)
    for i in range(5):
        if calif[i]>mayor:
            mayor = calif[i]
    menor = calif[0]        
    for i in range(5):
        if calif[i]<menor:
            menor=calif[i]
    print("El número mayor es: " + str(mayor) + "\n" + "El número menor es: " + str(menor) + "\n" + "El promedio de calificaciones es: " + str(suma/len(calif)))                


if __name__ == '__main__':
    calificaciones()





""" 4.4 Ejercicio 4 (1.2 puntos)
Codifica un programa en python que nos permita guardar los nombres de los
alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listados con las notas de cada alumno.
El programa pedirá el número de alumnos que vamos a introducir, pedirá su
nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error. """

def alumnos():
    lista = {}
    listaFin = {}
    calif = []
    name =''
    a = 0
    promedio = 0
    numAlumnos = int(input("Ingrese el número de alumnos: "))
    while len(lista)<=numAlumnos-1:
        calif=[]
        name = input("Ingrese el nombre del alumno: ")
        if name in lista:
            print("Ingresa otro nombre, por favor, ese ya está")
            continue
        lista.setdefault(name,calif)
        while a!=-1:
            suma = 0
            print("Escribe -1 para dejar de agregar calificaciones \n")
            a = input("Ingrese calificación: ")
            suma += int(a)
            calif.append(int(a))
            for i in range(len(calif)-1):
                suma += calif[i]
            if int(a) == -1:
                calif.remove(-1)
                promedio = float(suma/len(calif))
                listaFin.setdefault(name,promedio)
                break      
    print(listaFin)            
    
if __name__ == '__main__':
    alumnos()




""" 4.5 Ejercicio 5 (1.2 puntos)
Crea una tupla con los meses del año, pide números al usuario, si el número está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero. """

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

def mes():
    a = int(input("Ingrese un número de mes: "))
    if (a<1 or a>12):
        print("Número equivocado, no hay un mes con ese valor")
    else:
        b = a - 1
        print(meses[b])     

    
if __name__ == '__main__':
    mes()


