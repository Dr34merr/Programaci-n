#Contador de vocales
frase = input("Ingresa una frase para poder contar cuántas veces aparece cada vocal: ").lower()
vocales = ["a", "e", "i", "o", "u"]
veces = []

for vocal in vocales:
    veces.append(frase.count(vocal))

print(vocales,veces,end="\t")
