import random
n = 2000
m = 2000
A = []
for x in range(n):
    A.append([])
    for y in range(m):
        A[x].append(random.randint(0,100))
B = []
for x in range(m):
    B.append([])
    for y in range(n):
        B[x].append(random.randint(0,100))

archivoA = open("A2000.txt",'w')
for fila in A:
            archivoA.write(' '.join(map(str, fila)) + '\n')
archivoB = open("B2000.txt",'w')           
for fila in B:
            archivoB.write(' '.join(map(str, fila)) + '\n') 
archivoA.close()
archivoB.close()
