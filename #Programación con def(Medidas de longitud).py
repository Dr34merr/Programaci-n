#Programación con def
print("Este programa tiene la función de convertir los valores a otros valores que busques, primero ingresa que \
      tipo de dato es (Pies=ft, Yardas=yd, Pulgadas=in, Centímetro=cm o Metro=m), y posteriormente que cantidad de longitud es: ")
tipo=str(input("Ingrese que tipo de dato es: "))
longitud=float(input("ingrese el valor de la longitud: "))

def pies(longitud):
    yarda1=longitud/3
    pulgada1=longitud*12
    centimetros1=longitud*30.48
    metros1=longitud/3.281
    print("El resultado de ",longitud,"ft son: ",yarda1,"yd, ",pulgada1,"in, ",centimetros1,"cm y ",metros1,"m.")
    return longitud

def yarda(longitud):
    pies2=longitud*3
    pulgada2=longitud*36
    centimetros2=longitud*91.44
    metros2=longitud/1.094
    print("El resultado de ",longitud,"yd son: ",pies2,"ft, ",pulgada2,"in, ",centimetros2,"cm y ",metros2,"m.")
    return longitud

def pulgadas(longitud):
    pies3=longitud/12
    yarda3=longitud/36
    centimetros3=longitud*2.54
    metros3=longitud/39.37
    print("El resultado de ",longitud,"in son: ",pies3,"ft, ",yarda3,"yd, ",centimetros3,"cm y ",metros3,"m.")
    return longitud

def centimetros(longitud):
    pies4=longitud/30.48
    yarda4=longitud/91.44
    pulgada4=longitud/2.54
    metros4=longitud/100
    print("El resultado de ",longitud,"cm son: ",pies4,"ft, ",yarda4,"yd, ",pulgada4,"in y ",metros4,"m.")
    return longitud

def metros(longitud):
    pies5=longitud*3.281
    yarda5=longitud*1.094
    pulgada5=longitud*39.37
    centimetros5=longitud*100
    print("El resultado de ",longitud,"m son: ",pies5,"ft, ",yarda5,"yd, ",pulgada5,"in y ",centimetros5,"cm.")
    return longitud

if tipo=="ft":
    pies(longitud)
elif tipo=="yd":
    yarda(longitud)
elif tipo=="in":
    pulgadas(longitud)
elif tipo=="cm":
    centimetros(longitud)
elif tipo=="m":
    metros(longitud)
else:
    print("No ingreso una medida de longitud valida")