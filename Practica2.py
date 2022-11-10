""" 2.1 Ejercicio 1
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius. Recordar que la fórmula para la conversión es: """

fahrenheit = int(input('Ingrese una temperatura en grados Fahrenheit: '))

#fórmula para la conversión
celsius = (5/9) * (fahrenheit - 32)

# Hacemos uso de la funcion str.format() para darle formato a nuestra respuesta
print('{} grados Fahrenheit son {} grados Celsius '.format(fahrenheit, celsius))




""" 2.2 Ejercicio 2
Dados dos números, mostrar la suma, resta, división y multiplicación de ambos. """

numero1 = int(input("ingrese un número "))
numero2 = int(input("ingrese otro numero "))
operacion = input("1.- suma, 2.- resta, 3.- división, 4.- multiplicación\n")

if operacion == "1":
   print(numero1 + numero2)
elif operacion == "2":
   print(numero1 - numero2)
elif operacion == "3":
   print(numero1 / numero2)
elif operacion == "4":
   print(numero1 * numero2)



""" 2.3 Ejercicio 3
Calcular el perímetro y área de un rectángulo dada su base y su altura. """

base=float(input("Dime la base:"))
altura=float(input("Dime la altura:"))
perimetro = 2*base + 2*altura
area = base * altura
print ("Resultado: Area=%.2f Perimetro=%.2f" % (area,perimetro))



""" 2.4 Ejercicio 4
Calcular la media de tres números pedidos por teclado. """

print('Media de 3 numeros')
x=float(input('''Numero 1              '''))
y=float(input('''Numero 2              '''))
z=float(input('''Numero 3              '''))

promedio = float (x+y+z)/3
print('El promedio es ', promedio)





