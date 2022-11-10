""" 7.1 Ejercicio 1 (2 puntos)
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
● Un constructor, donde los datos pueden estar vacíos.
● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
● mostrar(): Muestra los datos de la persona.
● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad. """

class Persona:
    def __init__(self):
        pass
    def __init__(self, nombre, edad, DNI):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad=edad
    @property
    def DNI(self):
        return self.__DNI
    @DNI.setter
    def DNI(self, DNI):
        self.__DNI=DNI
    def mostrar(self):
        return "Nombre: " + str(self.nombre) + " Edad: " + str(self.edad) + " DNI: " + str(self.DNI)
    def esMayorEdad(self):
        return print(self.edad>=18)                       


""" 7.2 Ejercicio 2 (2 puntos)
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
● Un constructor, donde los datos pueden estar vacíos.
● Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
● mostrar(): Muestra los datos de la cuenta.
● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos. """

class Cuenta:
    
    def __init__(self, titular, cantidad = 0):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular=titular
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad=cantidad
    
    def mostrar(self):
        return "Titular: " + str(self.__titular) + " Cantidad: " + str(self.__cantidad)
    def ingresar(self, cantidad):
        if cantidad>0:
            self.__cantidad += cantidad
    def retirar(self, cantidad):
        self.__cantidad-=cantidad        


""" 7.3 Ejercicio 3 (2 puntos)
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase Cuenta Joven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:
● Un constructor.
● Los setters y getters para el nuevo atributo.
● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad;, por lo tanto hay que crear un método es Titular Válido ( ) que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
● Además la retirada de dinero sólo se podrá hacer si el titular es válido.
● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
● Piensa los métodos heredados de la clase madre que hay que reescribir. """

class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad = 0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion

    def esTitularValido(self):
        return (self.titular.edad>18) and (self.titular.edad<25)

    def retirar(self, cantidad):
        if self.esTitularValido():
            self.__cantidad-=cantidad
        else:
            print("Usuario no válido, no se puede retirar")                    
    def mostrar(self):
        return "Cuenta Joven \n" + super().mostrar() + " Bonificación: " + str(self.__bonificacion)        




