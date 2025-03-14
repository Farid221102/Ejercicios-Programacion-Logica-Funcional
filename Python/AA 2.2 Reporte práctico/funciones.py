#EJEMPLO CALLBACK
def operar(n1, n2, funcion):
    return funcion(n1, n2)

def suma(a,b): #Función de primer orden
    return a + b

def resta(a,b):
    return a - b

resultado = operar(5, 3, suma) #La función suma actua como callback al ejecutarse en operar
print(resultado)

resultado = operar(5, 3, resta) #La función resta actua como callback al ejecutarse en operar
print(resultado)

'''Un callback es una función que se pasa a otra función como argumento y se espera que sea llamada dentro de esa función
Las funciones de primer orden son aquellas que no toman otras funciones como argumentos ni devuelven funciones'''


#EJEMPLO FUNCIÓN PRIMERA CLASE
def saludo():
    return "¡Hola!"

mi_variable = saludo  # Asignamos la función a una variable
print(mi_variable())  # Llamamos a la función a través de la variable

def saludo2():
    return "¡Que tal!"

mi_variable = saludo2  # Asignamos la función a una variable
print(mi_variable())  # Llamamos a la función a través de la variable

'''Una función de primera clase puede ser asignada a una'''


#EJEMPLO FUNCIÓN DE ORDEN SUPERIOR
def elegir_operacion(operacion): #Funcion de orden superior
    def multiplicar(x):
        return x * 2
    def dividir(x):
        return x / 2
    if operacion == "Multiplicar":
        return multiplicar #Retornamos la función sin ejecutarla
    else:
        return dividir
    
doble = elegir_operacion("Multiplicar")
print(doble(10))
divide2 = elegir_operacion("Dividir")
print(divide2(10))

'''Una función de orden superior es auqella que puede recibir otras funciones
como argumentos o devolver una función como resultado'''


#EJMPLO FUNCIÓN ANÓNIMA = LAMBDA
doble = lambda x: x * 2
print(doble(5))

numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros)) 
print(dobles)

alumnos = ['Alejandro', 'Miguel', 'Vinicio', 'Rodney', 'Marcial']
saludar_alumnos = list(map(lambda nombre: 'Hola ' + nombre, alumnos))
print(saludar_alumnos)

#Sin lambda
def saludar(nombre):
    return 'Hola ' + nombre

#Usamos map con la función saludar
lista_saludos = list(map(saludar, alumnos))
print(lista_saludos)