#Piedra, Papel o Tijera
print("Juguegos piedra, papel, tijera, si deseas salir ingresa ya sea jugador 1 o 2 la palabra -salir-; Ya conocen las reglas del juego así que comenzemos: ")
jugador1=str(input("Ingrese que desea tirar jugador uno: "))
jugador2=str(input("Ingrese que desea tirar jugador dos: "))
w1j=int()
w2j=int()
#def Piedra_Papel_o_Tijera(jugador1,jugador2):

if (jugador1==jugador2):
    print("empate")
elif (jugador1=="piedra") and (jugador2=="tijera") or (jugador1=="papel") and (jugador2=="piedra") or (jugador1=="tijera") and (jugador2=="papel"):
    print("Jugador uno gana")
else:
    print("Jugador dos gana")
