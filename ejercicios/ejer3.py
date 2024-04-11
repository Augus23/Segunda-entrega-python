"""En este modulo hago un recorrido de la lista de jugadores donde utilizo la variable total_points que me
guarda la cantidad de puntos por jugador, en caso de q me aparezca un jugador con mas puntos reemplazo en la
variable more_influent_player el nombre y su puntaje"""

def main(players_list):
    more_influent_player = ["",-1]

    for player in players_list:
        total_points = (player[1]*1.5) + (player[2]*1.25) + (player[3])
        if total_points > more_influent_player[1]:
            more_influent_player[0] = player[0]
            more_influent_player[1] = total_points

    return more_influent_player