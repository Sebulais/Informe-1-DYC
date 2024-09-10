import time
def bubble_sort(arr):

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

inicio = time.time()

with open("datasetOrdenado.txt", "r") as file:
    contenido = file.read()
    numeros = [int(num) for num in contenido.split()]

bubble_sort(numeros)

fin = time.time()
tiempo = fin - inicio
print(tiempo)