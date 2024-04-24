#Par e Inpar
num=()
num_par=0
num_impar=0

while num!=0:
    num=int(input("Ingrese un numero, para terminar ingresa 0: "))
    if num%2 == 1:
        num_par= num_par+1
    else:
        num_impar= num_impar+1
print("El total de numeros pares es: ", num_par)
print("El total de numeros impares es: ", num_impar)