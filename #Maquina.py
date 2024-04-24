# Diccionario con las denominaciones de billetes y su valor en quetzales (moneda de Guatemala)
billetes_guatemala = {
    1: 1,    # Billete de 1 quetzal
    5: 5,    # Billete de 5 quetzales
    10: 10,  # Billete de 10 quetzales
    20: 20,  # Billete de 20 quetzales
    50: 50,  # Billete de 50 quetzales
    100: 100  # Billete de 100 quetzales
}

def calcular_cambio(monto_a_pagar, cantidad_pagada):
    if cantidad_pagada < monto_a_pagar:
        print("La cantidad pagada es insuficiente. ¡Debe pagar al menos el monto a pagar!")
        return

    cambio_total = cantidad_pagada - monto_a_pagar
    print(f"Cambio total: {cambio_total} quetzales")

    # Desglosar el cambio en billetes
    for billete, valor in sorted(billetes_guatemala.items(), reverse=True):
        cantidad_billetes = cambio_total // valor
        if cantidad_billetes > 0:
            print(f"{cantidad_billetes} billetes de {valor} quetzales")
            cambio_total -= cantidad_billetes * valor

# Solicitar el monto a pagar y la cantidad pagada
monto_a_pagar = float(input("Ingrese el monto a pagar (en quetzales): "))
cantidad_pagada = float(input("Ingrese la cantidad con la que se pagó (en quetzales): "))

# Calcular y mostrar el cambio
calcular_cambio(monto_a_pagar, cantidad_pagada)