""" 6.1 Ejercicio 1 (1.5 puntos)
Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”. """

def menu():
    print('''
    //////////////////////////////
                Menú
    1. Sopa de Fideos
    2. Spaghetti
    3. Lasagna

    4. Bistec
    5. Tacos dorados
    6. Pastel de carne
    //////////////////////////////
    Para salir del menú escriba salir           
    ''')
    a = input("Seleccione su platillo: ")
    if a == "salir":
        print("Salió del Menú")
    else:
        switcher = {
            1: "Has escogido Sopa de Fideos",
            2: "Has escogido Spaghetti",
            3: "Has escogido Lasagna",
            4: "Has escogido Bistec",
            5: "Has escogido Tacos dorados",
            6: "Has escogido Pastel de carne",
        }    
        print(switcher.get(int(a), "Platillo inválido"))


if __name__ == '__main__':
    menu()


""" 6.2 Ejercicio 2 (1.5 puntos)
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar. """

def primos():
    flag = 0
    N = int(input("Introduce la cantidad de primos que quieras: "))
    filtro=[]
    arr=[2]
    output=[]
    for i in range(2,300):
        for j in range(len(arr)):
            if i%arr[j]==0:
                break
            else:
                arr.append(i)
                arr=list(set(arr))
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                continue
            else:
                if arr[i]%arr[j]==0:
                    filtro.append(arr[i])
                    filtro=list(set(filtro))
    for m in range(len(filtro)):
            arr.remove(filtro[m])
    for k in range(N):
            output.append(arr[k])
    print(output)
                                

if __name__ == '__main__':
    primos()

""" 6.3 Ejercicio 3 (1.5 puntos)
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses. """

def pago():
    pago = 10
    total = pago
    print("El pago del mes: 1 es igual a : " + str(pago))
    for i in range(19):
        pago*=2
        total+=pago
        print("El pago del mes: " + str(i+2) + " es igual a: " + str(pago))
    print("El pago total fue: " + str(total))    

if __name__ == '__main__':
    pago()



""" 6.4 Ejercicio 4 (1.5 puntos)
Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120). """

def factorial():
    n=int(input("Introduzca un número para obtener su factorial: "))
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(str(n)+"! = " + str(fact))
if __name__ == '__main__':
    factorial()        



