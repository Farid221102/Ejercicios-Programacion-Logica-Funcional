#Tipos de datos
#Colecciones

#Listas
print("----- LISTAS -----")
lista = [1,2,3,4,5]
print(lista)
print("Primer elemento:")
print(lista[0]) #Imprime el primer elemento de la lista
print("Segundo elemento:")
print(lista[1])

#Tuplas
print("\n----- TUPLAS -----")
tupla = [1,2,3,4,5]
print(tupla)
print("Primer elemento:")
print(tupla[0]) #Imprime el primer elemento de la lista
print("Segundo elemento:")
print(tupla[1])

#Diccionarios
print("\n----- DICCIONARIOS -----")
diccionario = {'nombre': 'Juan' ,'edad': 22}
print(diccionario)
print(diccionario['nombre']) #Imprime el valor de la clave nombre
print(diccionario['edad'])

#Conjuntos
print("\n----- CONJUNTOS -----")
conjunto = {1,2,3,4,5}
print(conjunto)

#Convertir cadena a entero
print("\n----- CADENA A ENTERO -----")
numero = int("10")
print(numero)

#Convertir cadena a flotante
print("\n----- CADENA A FLOTANTE -----")
numero = float("10.5")
print(numero)

#Convertir entero a cadena
print("\n----- ENTERO A CADENA -----")
numero = str(10)
print(numero)

#Convertir  flotante a cadena
print("\n----- FLOTANTE A CADENA -----")
numero = str(10.5)
print(numero)

#Convertir entero a flotante
print("\n----- ENTERO A FLOTANTE -----")
numero = float(10)
print(numero)

#Convertir  flotante a entero
print("\n----- FLOTANTE A ENTERO -----")
numero = int(10.5)
print(numero)

#Operaciones aritméticas
print("\n----- OPERACIONES ARITMÉTICAS -----")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)

#Operaciones relacionales
print("\n----- OPERACIONES RELACIONALES -----")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
print("¿El primer número es mayor que el segundo?:", num1 > num2)
print("¿El primer número es menor que el segundo?:", num1 < num2)
print("¿El primer número es mayor o igual que el segundo?:", num1 >= num2)
print("¿El primer número es menor o igual que el segundo?:", num1 <= num2)
print("¿El primer número es igual que el segundo?:", num1 == num2)
print("¿El primer número es diferente que el segundo?:", num1 != num2)

#Operaciones lógicas
print("\n----- OPERACIONES LÓGICAS -----")
print("AND")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)

print("\nOR")
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)

print("\nNOT")
print("Not True:", not True)
print("Not False:", not False)

#Operaciones de asignación
print("\n----- OPERACIONES DE ASIGNACIÓN -----")
num1 = 10
print("Valor inicial:", num1)
num1 += 5
print("Suma:", num1)
num1 -= 5
print("Resta:", num1)
num1 *= 5
print("Multiplicación:", num1)
num1 /= 5
print("División:", num1)
num1 %= 5
print("Residuo:", num1)
num1 **= 5 #Exponente
print("Exponente:", num1)
num1 //= 5 #División entera
print("Dvisión entera:", num1)

#operaciones de pertenencia
print("\n----- OPERACIONES DE PERTENENCIA -----")
lista = [1,2,3,4,5]
print(1 in lista)
print(6 in lista) #Imprime False
print(1 not in lista) #Imprime False
print(6 not in lista)

print("\n----- ¿APROBADO O REPROBADO? -----")
aprobado = float(input("Ingresa tu calificación: ")) >= 70
print("¿Aprobaste?:", aprobado)