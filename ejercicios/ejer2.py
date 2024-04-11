"""En este modulo utilizo la funcion lambda junto con la funcion reduce de la biblioteca functools para
encontrar el jugador con mayor goles en la lista players_list"""
from functools import reduce

def main(players_list):
    striker = reduce(lambda player1,player2: player1 if player1[1]>player2[1] else player2,players_list)
    return striker