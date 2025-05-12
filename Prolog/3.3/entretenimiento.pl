% Base de conocimientos
:- dynamic respuesta/2.

% Actividades físicas
actividad(basquet, 'Es excelente para el trabajo en equipo y la resistencia.') :-
    fisica, equipo.
actividad(gimnasio, 'Ideal para mejorar la fuerza y mantenerse en forma.') :-
    fisica, individual.

% Actividades recreativas
actividad(peliculas, 'Perfecta para relajarse y disfrutar una historia.') :-
    recreativa, audio_visual.
actividad(manualidades, 'Estimula la creatividad y la motricidad fina.') :-
    recreativa, artistica.
actividad(musica, 'Desarrolla la disciplina y la expresión emocional.') :-
    recreativa, practica.

% Limpia respuestas guardadas
limpiar_respuestas :-
    retractall(respuesta(_, _)).

% Realiza las preguntas
preguntar(Pregunta, Clave) :-
    (respuesta(Clave, Resp) ->  Resp = s    ;  
    write(Pregunta), nl, read(R), asserta(respuesta(Clave, R)), R = s).

% Clasificación general
fisica     :- preguntar('¿Deseas una actividad física?', fisica).
recreativa :- \+ fisica.

% Subpreguntas para actividades físicas
equipo     :- preguntar('¿Prefieres un deporte en equipo?', equipo).
individual :- \+ equipo.

% Subpreguntas para actividades recreativas
audio_visual :- preguntar('¿Deseas algo audiovisual?', audiovisual).
artistica     :- preguntar('¿Deseas algo artístico?', artistica).
practica      :- preguntar('¿Deseas algo que requiera práctica constante?', practica).

% Inicio del programa
iniciar :-
    repeat,
    limpiar_respuestas,
    nl, write('--- Sistema de recomendaciones de actividades de entretenimiento ---'),
    nl, write('Responde con s. / n.'), nl, nl,
    (actividad(X, Msg) -> nl, write('La actividad recomendada es: '), write(X), nl, write('Observación: '), write(Msg), nl
    ;   nl, write('No se encontró una actividad que coincida :('), nl),
    nl, write('¿Quieres intentarlo de nuevo?'), nl,
    read(R),
    R \= s, !,
    nl, write('Fin del programa.'), nl.