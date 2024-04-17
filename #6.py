#6
contrase_correcta=("1nc0rr3ct4")
intentos=0

while intentos<100000000:
    contraseña=str(input("Ingrese la contraseña: "))
    if  contraseña == contrase_correcta:
        print("Bienvenido")
        break
    else:
        print("contraseña incorrecta")
    
    intentos+=1

