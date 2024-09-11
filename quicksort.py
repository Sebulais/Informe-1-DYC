import time, random  
def quicksort(arr, start , stop):
    if(start < stop):
         
        pivotindex = partitionrand(arr,\
                             start, stop)
         

        quicksort(arr , start , pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)
 

def partitionrand(arr , start, stop):
 

    randpivot = random.randrange(start, stop)
 

    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)
 

def partition(arr,start,stop):
    pivot = start 
     

    i = start + 1


    for j in range(start + 1, stop + 1):
         

        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
with open("datadesordenado.txt", "r") as archivo:
    leer = archivo.read()
    numeros = [int(n) for n in leer.split()]
inicio = time.time()
quicksort(numeros, 0, len(numeros) - 1)
final = time.time()
print(numeros)
print(final-inicio)

