#Registro de cambio
pago=int(input("Ingrese la cantidad a pagar: "))
cuota=int(input("Ingrese la cantidad del pago: "))
cambio=int()
#Billetes
Q100=int()
Q50=int()
Q20=int()
Q10=int()
Q5=int()
Q1=int()

def Verificación_de_Rango (pago):
    if 0<pago<200+1:
        if pago<0:
            print("Por favor pagar con targeta")
        elif pago>200:
            print("Pagar con targeta")