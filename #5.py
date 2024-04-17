#5
num=int()
num=int(input("Ingrese el numero hasta donde quiere inicar el conteo hasta cero: "))

if 0<num:
    for i in range (num,0,-1):
        print(i,",", end="\t")