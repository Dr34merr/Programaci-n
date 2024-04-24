#Contraseña de 3 intentos
contrase_correcta=("1nc0rr3ct4")
intentos=-3

while intentos<0:
    contraseña=str(input("Ingrese la contraseña: "))
    if contraseña == ("salir"):
        print("Vuelva pronto")
    elif contraseña == contrase_correcta:
        print("Bienvenido")
    else:
        intentos= intentos+1
print("Se terminaron los intentos")
