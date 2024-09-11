import time
with open("dataordenado.txt", "r") as archivo:
    leer = archivo.read()
    numeros = [int(num) for n in leer.split()]
inicio = time.time()
numeros.sort()
final = time.time()
print(numeros)
print(final-inicio)
