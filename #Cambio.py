#Cambio

billetes_guatemala = {
    0.01: 0.01,
    0.10: 0.10,
    0.25: 0.25,
    0.50: 0.50,
    1: 1,    
    5: 5,    
    10: 10,  
    20: 20,  
    50: 50,  
    100: 100,
    200: 200
}

def calcular_cambio(monto,pago):
    if pago < monto:
        print("La cantidad pagada es insuficiente. ¡Debe pagar al menos el monto!")
        return

    cambio_total = pago - monto
    print(f"Cambio total: {cambio_total} quetzales")

    for billete, valor in sorted(billetes_guatemala.items(), reverse=True):
            cantidad_billetes = cambio_total// valor
            if cantidad_billetes > 0:
                print(f"{cantidad_billetes} billetes de {valor} quetzales")
            cambio_total -= cantidad_billetes * valor

monto=float(input("Ingrese el monto a pagar del cliente: "))
pago=float(input("Ingrese la cantidad con la que se pagó: "))


calcular_cambio(monto,pago)
