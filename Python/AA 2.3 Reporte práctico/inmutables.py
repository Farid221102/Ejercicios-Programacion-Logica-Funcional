"""
Uno de los principios fundamentales de la programación funcional es no cambiar nada.
Los cambios conducen a errores.
Es más fácil prevenirlos sabiendo que las funciones no cambian nada, ni
siquiera sus argumentos ni ninguna variable global.

En progrmación funcional, cambiar o alterar algo se denomina mutación, 
y el resultado se denomina efecto secundario.
Idealmente, una funci+on debería ser una función pura, es decir, que no cause efectos secundarios.
"""

#Ejemplo 1. Inmutabilidad, función pura y sin efectos secundarios
variable_global = 10

def aumentar_variable ():
    return variable_global + 1

print(aumentar_variable())

#Ejemplo 3. Uso incorrecto de la función pura
contador_global = 0

def contar_palabras_no_funcional(texto):
    global contador_global
    contador_global = len(texto.split())

texto_ejemplo = "Este es un ejemplo sencillo"
contar_palabras_no_funcional(texto_ejemplo)