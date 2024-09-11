import random, time
A = []
archivoA = open("A1024.txt", 'r')
for linea in archivoA:
    fila = list(map(int, linea.split()))
    A.append(fila) 
B = []
archivoB = open("B1024.txt", 'r')
for linea in archivoB:
    fila = list(map(int, linea.split()))
    B.append(fila)
archivoB.close()
archivoA.close()

inicio = time.time()
def multiplicar_matrices(m1, m2):
    if len(m1[0]) == len(m2):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)
        
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    m3[i][j] += m1[i][k] * m2[k][j]

        return m3
result= multiplicar_matrices(A,B)
final = time.time()
print(result)
print(final - inicio)
