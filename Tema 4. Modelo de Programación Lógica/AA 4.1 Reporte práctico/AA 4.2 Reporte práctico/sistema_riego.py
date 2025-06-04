#Datos para cada zona
humedad = {
    'norte': 'baja',
    'sur': 'baja',
    'centro': 'baja'
}

temperatura = {
    'norte': 34,
    'sur': 30,
    'centro': 36
}

pronostico_lluvia = {
    'norte': False,
    'sur': False,
    'centro': True
}

hora = 19

#Funciones del sistema
def hora_adecuada(hora):
    return hora < 10 or hora > 18

def regar(zona):
    if humedad[zona]=='baja' and pronostico_lluvia[zona]==False and hora_adecuada(hora):
        return True
    return False

def estado(zona):
    if regar(zona):
        return 'Activado'
    else:
        return 'No activado'

def alerta(zona):
    return temperatura[zona] >= 32

def recomendacion(zona):
    if regar(zona) and alerta(zona):
        return 'ALERTA: Riego activado con temperatura alta. Considere regar de noche o por goteo'
    elif regar(zona):
        return 'Sin recomendaciones especiales para el riego'
    else:
        return 'No es necesario activar el riego. Está lloviendo'

def mostrarInfo():
    for zona in humedad:
        print(f"Zona: {zona}")
        print(f"Estado: {estado(zona)}")
        print(f"Recomendación: {recomendacion(zona)}")
        print()

mostrarInfo()