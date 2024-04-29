# #1
# contraseña = input("Introduce la contraseña: ")
# if contraseña in ("sesamo"):
#   print("Pasa")
# else:
#   print("No pasa")
#Solo corregir algunos signos

#2
# base = float(input('Introduce la base imponible de la factura: '))
# iva=0.12

# def aplica_iva(base, iva = 21):
#     base = base * iva   
#     return base 

# print(aplica_iva(base, iva))
#Agregar float, y agregar el valor del iva

# #3
# u = {1, 2, 3}
# v = {4, 5, 6}

# def producto_escalar(u, v):
#     sum=(0)
#     for ui, vi in zip(u,v):
#         sum += ui * vi
#     return sum

# print(producto_escalar(u, v))
#Solo ver el metodo de trabajar original y arreglarlo conforme a ello, agregar donde se guardara el resultado\
#el for debe de tener los dos grupos de U y V el zip, para poder usar la dupla.

#4
# listin = {'Juan':123456789, 'Pedro':987654321}

# def elimina(listin, usuario):
#     if usuario in listin:
#         del listin[usuario]
#         return "Usuario eliminado correctamente."
#     else:
#         return "El usuario no existe en el listin."

# usuario_a_eliminar = 'Pedro'
# print(elimina(listin, usuario_a_eliminar))
# print(listin)
#hay que arreglar cosas como que primero if tiene un usuario, que mande algunos mensajes de retorno; agregar\
#usuario a eliminar para determinar el usuario.
    
###CORREGUIR 5###
a = ((1, 2, 3),
     (3, 2, 1))
b = ((1, 2),
     (3, 4),
     (5, 6))

def producto(a, b):
    producto = []
    for i in range(len(a)):
        fila = []
        for j in range(len(b[0])):
            suma = 0
            for k in range(len(a[0])):
                suma += a[i][k] * b[k][j]
            fila.append(suma)
        producto.append(tuple(fila))
    return tuple(producto)

print(producto(a,b))
#Unicamente hay que quitar algunas cosas como por ejemplo los +1, cambiar alguna posiciones con respecto a fila\
#donde se debe cambiar por la a y en el otro por la b y ordenar algunos datos más, en el caso de el trabajo\
#en suma a y b en el apartado de K tienen que tener el mismo valor, por lo que se le cambian algunas posiciónes\
#por ultimo es unicamente poner un print donde lo invocamos.