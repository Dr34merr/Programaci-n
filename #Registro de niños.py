#Registro de niños
print("Esta aplicación es para el registro y clasificación de los niños y niñas para sus respectivas aulas")
print("El registro sera: Los de 4 años son de Pre-kinder, Los de 5 años son de kinder, Los de 6 años son de Preparatoria")
#Preguntas
n1=int(input("Ingrese la edad del 1 niño: "))
n2=int(input("Ingrese la edad del 2 niño: "))
n3=int(input("Ingrese la edad del 3 niño: "))
n4=int(input("Ingrese la edad del 4 niño: "))
n5=int(input("Ingrese la edad del 5 niño: "))
n6=int(input("Ingrese la edad del 6 niño: "))
n7=int(input("Ingrese la edad del 7 niño: "))
n8=int(input("Ingrese la edad del 8 niño: "))
n9=int(input("Ingrese la edad del 9 niño: "))
n10=int(input("Ingrese la edad del 10 niño: "))
#Contadores
prekinder=int()
kinder=int()
preparatoria=int()
no_ingresan=int()

#procesos
if (3<n1<7):
    if (n1==4):
        prekinder = prekinder + 1
    elif (n1==5):
        kinder = kinder + 1
    elif (n1==6):
        preparatoria = preparatoria + 1
else:
    no_ingresan = no_ingresan + 1

if (3<n2<7):
    if (n2==4):
        prekinder = prekinder + 1
    elif (n2==5):
        kinder = kinder + 1
    elif (n2==6):
        preparatoria = preparatoria + 1
else:
    no_ingresan = no_ingresan + 1

if (3<n3<7):
    if (n3==4):
        prekinder = prekinder + 1
    elif (n3==5):
        kinder = kinder + 1
    elif (n3==6):
        preparatoria = preparatoria + 1
else:
    no_ingresan = no_ingresan + 1

if (3<n4<7):
    if (n4==4):
        prekinder = prekinder + 1
    elif (n4==5):
        kinder = kinder + 1
    elif (n4==6):
        preparatoria = preparatoria + 1
else:
    no_ingresan = no_ingresan + 1

if (3<n5<7):
    if (n5==4):
        prekinder = prekinder + 1
    elif (n5==5):
        kinder = kinder + 1
    elif (n5==6):
        preparatoria = preparatoria + 1
else:
    no_ingresan = no_ingresan + 1

if (3<n6<7):
    if (n6==4):
        prekinder = prekinder + 1
    elif (n6==5):
        kinder = kinder + 1
    elif (n6==6):
        preparatoria = preparatoria + 1
else:
    no_ingresan = no_ingresan + 1

if (3<n7<7):
    if (n7==4):
        prekinder = prekinder + 1
    elif (n7==5):
        kinder = kinder + 1
    elif (n7==6):
        preparatoria = preparatoria + 1
else:
    no_ingresan = no_ingresan + 1

if (3<n8<7):
    if (n8==4):
        prekinder = prekinder + 1
    elif (n8==5):
        kinder = kinder + 1
    elif (n8==6):
        preparatoria = preparatoria + 1
else:
    no_ingresan = no_ingresan + 1

if (3<n9<7):
    if (n9==4):
        prekinder = prekinder + 1
    elif (n9==5):
        kinder = kinder + 1
    elif (n9==6):
        preparatoria = preparatoria + 1
else:
    no_ingresan = no_ingresan + 1

if (3<n10<7):
    if (n10==4):
        prekinder = prekinder + 1
    elif (n10==5):
        kinder = kinder + 1
    elif (n10==6):
        preparatoria = preparatoria + 1
else:
    no_ingresan = no_ingresan + 1

if no_ingresan>0:
    print("Los que no ingresan son: ",no_ingresan)
    print("Los que ingresan a Pre-kinder son: ",prekinder)
    print("Los que ingresan a kinder son: ",kinder)
    print("Los que ingresan a Preparatoria son: ",preparatoria)
else:
    print("Los que ingresan a Pre-kinder son: ",prekinder)
    print("Los que ingresan a kinder son: ",kinder)
    print("Los que ingresan a Preparatoria son: ",preparatoria)