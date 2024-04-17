#4
num=int()
num=int(input("Ingrese el numero hasta donde quiere terminar de ver todos los numeros impares: "))

for i in range (1,num+1):
    if i%2!=0:
        print(i,",",end="\t")    