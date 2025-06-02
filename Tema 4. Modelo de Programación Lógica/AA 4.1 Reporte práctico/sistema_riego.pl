% Se tendrán las zonas norte, sur y centro
% Hechos
humedad(norte, baja).
humedad(sur, baja).
humedad(centro, baja).

temperatura(norte, 34).
temperatura(sur, 30).
temperatura(centro, 36).

pronostico_lluvia(norte, false).
pronostico_lluvia(sur, false).
pronostico_lluvia(centro, true).

hora(19).

% Reglas
hora_adecuada :-   hora(H), (H < 10 ; H > 18).

regar(Zona) :- 
    humedad(Zona, baja),
    pronostico_lluvia(Zona, false),
    hora_adecuada.

estado(Zona, 'Activado') :- regar(Zona), !.
estado(Zona, 'No activado') :- \+ regar(Zona).

alerta(Zona) :-    temperatura(Zona, T), T >= 32.

recomendacion(Zona) :-
    regar(Zona),
    alerta(Zona), !,
    writeln('ALERTA: Riego activado con temperatura alta. Considere regar de noche o por goteo').

recomendacion(Zona) :-
    \+ regar(Zona), !,
    writeln('No es necesario activar el riego. Está lloviendo').

recomendacion(Zona) :- writeln(['Sin recomendaciones especiales para el riego', Zona]).