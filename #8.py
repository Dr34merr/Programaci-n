#8
palabra=str()
salir=("Salir")
intentos=0
while intentos<100000000:
    palabra=str(input("Ingresa una palabra, para salir escribe Salir: "))
    if  palabra==salir:
        print("Adios")
        break
    else:
        print(palabra)
    
    intentos+=1
