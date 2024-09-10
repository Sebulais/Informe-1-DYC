import time
with open("datasetOrdenado2.txt", "r") as file:
    contenido = file.read()
    numeros = [int(num) for num in contenido.split()]
inicio = time.time()
numeros.sort()
final = time.time()
print(numeros)
print(final-inicio)