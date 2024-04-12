"""Creo una lista de los jugadores con sus estadisticas ultilizando la funcion zip, recibiendo como parametro
las listas dadas en el ejercicio, el docstring de names lo convierto a lista utilizando el metodo split, luego
creo un zip asignandole las estadisticas a cada jugador y lo convierto a lista para despues recorrerlo varias
veces en los demas incisos. Lo utiizo para resolver el ejercicio1"""

def ejer1(names,goals,goals_avoided,assists):
    list_names = names.split(", ")
    players_list = list(zip(list_names,goals,goals_avoided,assists))
    return players_list

"""En este modulo utilizo la funcion lambda junto con la funcion reduce de la biblioteca functools para
encontrar el jugador con mayor goles en la lista players_list"""
from functools import reduce

def ejer2(players_list):
    striker = reduce(lambda player1,player2: player1 if player1[1]>player2[1] else player2,players_list)
    return striker

"""En este modulo hago un recorrido de la lista de jugadores donde utilizo la variable total_points que me
guarda la cantidad de puntos por jugador, en caso de q me aparezca un jugador con mas puntos reemplazo en la
variable more_influent_player el nombre y su puntaje"""

def ejer3(players_list):
    more_influent_player = ["",-1]

    for player in players_list:
        total_points = (player[1]*1.5) + (player[2]*1.25) + (player[3])
        if total_points > more_influent_player[1]:
            more_influent_player[0] = player[0]
            more_influent_player[1] = total_points

    return more_influent_player

"""En este modulo recibo la lista de el total de goles de los jugadores y utilizo la funcion sum para obtener
la suma de la lista y lo divido por la cantidad de partidos durante la temporada"""
def ejer4(goals):
    return sum(goals)/25

"""En este modulo recibo el dato obtenido del inciso 2 y divido sus goles por la cantidad de partidos
obteniendo el promedio de goles por partido"""
def ejer5(striker):
    striker_average = striker[1]/25
    return striker_average