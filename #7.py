#7
frase=str(input("Ingrese una frase de su preferencia: ")).lower
letra=str(input("ingrese una letra que quiera ver cuantas veces aparecen en la frase: "))

veces=frase.count(letra)
print("La letra ",letra," se repite ",": ",veces)