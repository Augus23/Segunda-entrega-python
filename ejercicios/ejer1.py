"""Creo una lista de los jugadores con sus estadisticas ultilizando la funcion zip, recibiendo como parametro
las listas dadas en el ejercicio, el docstring de names lo convierto a lista utilizando el metodo split, luego
creo un zip asignandole las estadisticas a cada jugador y lo convierto a lista para despues recorrerlo varias
veces en los demas incisos. Lo utiizo para resolver el ejercicio1"""

def main(names,goals,goals_avoided,assists):
    list_names = names.split(", ")
    players_list = list(zip(list_names,goals,goals_avoided,assists))
    return players_list