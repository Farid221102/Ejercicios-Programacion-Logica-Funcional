#Desafío Seleccionador ISC 🔍💻

""""
OBJETIVO
Desarrollar un programa en Python que simule al sombrero seleccionador, ayudando a los alumnos de ISC a descubrir cuál
de las ramas de sistemas computacionales es la más recomendable, basándose en sus respuestas a una serie de preguntas.

INSTRUCCIONES:
- El programa debe incluir al menos 5 preguntas que ayuden a identificar los intereses del alumno.
- Las ramas de sistemas computacionales a considerar son:
    A) Redes
    B) Bases de datos
    C) Desarrollo de software
    D) Programación hardware
    E) Modelado 3D
    F) Gestión de proyectos de software

Registrar puntajes:
- Cada respuesta debe sumar puntos a la rama correspondiente.
- Asegúrate de que las preguntas estén bien alineadas con las ramas.

El programa debe interactuar con el usuario a través de la consola, pidiéndole que responda a las preguntas.
"""

print('============')
print('Seleccionador ISC 🔍💻')
print('============')


redes = 0
bd = 0
soft = 0
hard = 0
modelado = 0
gestion = 0

#~~~~~~~~~~~~~~~~ Pregunta 1 #~~~~~~~~~~~~~~~~
print('P1) ¿Qué actividad disfrutas más?')
print(' 1) Configurar y administrar redes de computadoras.')
print(' 2) Diseñar bases de datos y consultas.')
print(' 3) Desarrollar aplicaciones y software.')
print(' 4) Trabajar con componentes físicos como circuitos y procesadores.')
print(' 5) Crear modelos 3D y animaciones.')
print(' 6) Coordinar equipos y planificar proyectos.')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    redes += 1
elif respuesta == 2:
    bd += 1
elif respuesta == 3:
    soft += 1
elif respuesta == 4:    
    hard += 1
elif respuesta == 5:    
    modelado += 1
elif respuesta == 6:    
    gestion += 1
else:
    print('Respuesta inválida')


#~~~~~~~~~~~~~~~~ Pregunta 2 #~~~~~~~~~~~~~~~~
print('\nP2) Si tuvieras que resolver un problema técnico, ¿cuál te interesaría más?')
print(' 1) Organizar y analizar grandes volúmenes de información.')
print(' 2) Diagnosticar y mejorar la seguridad en una red.')
print(' 3) Crear un modelo en 3D para una simulación o videojuego.')
print(' 4) Diseñar una aplicación eficiente y fácil de usar.')
print(' 5) Problemas de planificación y ejecución de proyectos tecnológicos.')
print(' 6) Programar un microcontrolador para una tarea específica.')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    bd += 1
elif respuesta == 2:
    redes += 1
elif respuesta == 3:
    modelado += 1
elif respuesta == 4:    
    soft += 1
elif respuesta == 5:    
    gestion += 1
elif respuesta == 6:    
    hard += 1
else:
    print('Respuesta inválida')


#~~~~~~~~~~~~~~~~ Pregunta 3 #~~~~~~~~~~~~~~~~
print('\nP3) ¿Qué tipo de herramientas o tecnologías te gustaría aprender a utilizar?')
print(' 1) Jira, Trello o Scrum.')
print(' 2) Blender, Maya o 3ds Max.')
print(' 3) MySQL, PostgreSQL o MongoDB.')
print(' 4) Arduino o FPGA.')
print(' 5) Cisco Packet Tracer o Wireshark.')
print(' 6) Python, Java o C#.')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    gestion += 1
elif respuesta == 2:
    modelado += 1
elif respuesta == 3:
    bd += 1
elif respuesta == 4:    
    hard += 1
elif respuesta == 5:    
    redes += 1
elif respuesta == 6:    
    soft += 1
else:
    print('Respuesta inválida')


#~~~~~~~~~~~~~~~~ Pregunta 4 #~~~~~~~~~~~~~~~~
print('\nP4) Si tuvieras que elegir un proyecto final, ¿cuál te gustaría más?')
print(' 1) Gestionar un proyecto con metodologías ágiles.')
print(' 2) Diseñar modelos 3D para un videojuego.')
print(' 3) Crear una aplicación web o móvil.')
print(' 4) Implementar una red segura y optimizada.')
print(' 5) Desarrollar un sistema de control para automatización industrial.')
print(' 6) Diseñar un sistema de bases de datos eficiente.')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    gestion += 1
elif respuesta == 2:
    modelado += 1
elif respuesta == 3:
    soft += 1
elif respuesta == 4:    
    redes += 1
elif respuesta == 5:    
    hard += 1
elif respuesta == 6:    
    bd += 1
else:
    print('Respuesta inválida')


#~~~~~~~~~~~~~~~~ Pregunta 5 #~~~~~~~~~~~~~~~~
print('\nP5) ¿En qué tipo de ambiente de trabajo te ves a futuro?')
print(' 1) En una empresa liderando equipos de desarrollo de software.')
print(' 2) En una empresa que maneje grandes volúmenes de información.')
print(' 3) En un estudio de diseño gráfico o desarrollo de videojuegos.')
print(' 4) En un centro de datos o empresa de telecomunicaciones.')
print(' 5) En una empresa de diseño y fabricación de hardware.')
print(' 6) En una empresa de desarrollo de software o como freelance.')

respuesta = int(input('Ingresa tu respuesta (1-6): '))

if respuesta == 1:
    gestion += 1
elif respuesta == 2:
    bd += 1
elif respuesta == 3:
    modelado += 1
elif respuesta == 4:    
    redes += 1
elif respuesta == 5:    
    hard += 1
elif respuesta == 6:    
    soft += 1
else:
    print('Respuesta inválida')


""""
Al final, el programa debe calcular cuál rama tiene el puntaje más alto y mostrarlo
"""
print("\nRedes: ", redes)
print("Bases de datos: ", bd)
print("Desarrollo de software: ", soft)
print("Programación hardware: ", hard)
print("Modelado 3D: ", modelado)
print("Gestión de proyectos de software: ", gestion)

print("")

max_puntaje = max(redes, bd, soft, hard, modelado, gestion)

if redes == max_puntaje:
    print("\n🌐 ¡Tu destino es Redes!")
elif bd == max_puntaje:
    print("\n📊 ¡Tu destino es Bases de datos!")
elif soft == max_puntaje:
    print("\n💻📱 ¡Tu destino es Desarrollo de software!")
elif hard == max_puntaje:
    print("\n🖥️🛠️ ¡Tu destino es Programación hardware!")
elif modelado == max_puntaje:
    print("\n🎨🖌️ ¡Tu destino es Modelado 3D!")
else:
    print("\n📋📈 ¡Tu destino es Gestión de proyectos de software!")