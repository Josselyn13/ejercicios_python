""" 8.1 Ejercicio 1 (2 puntos)
Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves. """

def diccionarioCuadrados():
    n=int(input("Escribe un numero: "))
    numeros={}
    for i in range(n):
        numeros[i+1]=((i+1)**2)
    print(numeros)    

if __name__ == '__main__':
    diccionarioCuadrados()

""" 8.2 Ejercicio 2 (2 puntos)
Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena. """

def diccionariocaracteres():
    frase = input("Escribe una frase: ")
    dic = {}
    frase = frase.replace(" ", " ")
    for i in range(len(frase)):
        a = frase[i:i+1]
        if a in dic:
            dic[a]=dic[a]+1
        else:
            dic[a]=1
    print(dic)            

if __name__ == '__main__':
    diccionariocaracteres()

""" 8.3 Ejercicio 3 (2 puntos)
Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta. """

def compraFrutas():
    answer = "si"
    while(answer == "si"):
        precioFrutas={"plátano": 30.32, "naranja": 14.50, "manzana": 17.80, "kiwi": 32.53, "sandía": 30.50}
        clave = input("¿Qué fruta desea comprar? ")
        cantidad = int(input("Indique cuántas frutas desea: "))
        if clave in precioFrutas:
            print("El pago total por la compra de " + clave + " es: $" + str(precioFrutas[clave]*cantidad))
            answer=input("¿Quiere continuar consultando? (Si/No): ")
            answer.lower()
        else:
            print("No tenemos esa fruta")
            answer=input("Quiere continuar consultando? (Si/No): ")
            answer.lower()    

if __name__ == '__main__':
    compraFrutas()


