import numpy as np
import time
 
def strassen(A, B):
    n = A.shape[0]
 
    # base case: 1x1 matrix
    if n == 1:
        return A * B
    else:
        # split input matrices into quarters
        mid = n // 2
        A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
        B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]
 
        # calculate p1 to p7
        P1 = strassen(A11 + A22, B11 + B22)
        P2 = strassen(A21 + A22, B11)
        P3 = strassen(A11, B12 - B22)
        P4 = strassen(A22, B21 - B11)
        P5 = strassen(A11 + A12, B22)
        P6 = strassen(A21 - A11, B11 + B12)
        P7 = strassen(A12 - A22, B21 + B22)
 
        # calculate the 4 quarters of the resulting matrix
        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 + P3 - P2 + P6
 
        # combine the 4 quarters into a single result matrix
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
 
        return C
 
def main(n1,n2):
    A = np.array(n1)
    B = np.array(n2)
 
    # Pad the matrices with zeros if necessary
    n = max(A.shape[0], A.shape[1], B.shape[0], B.shape[1])
    m = 1
    while m < n:
        m *= 2
    A = np.pad(A, ((0, m - A.shape[0]), (0, m - A.shape[1])), mode='constant')
    B = np.pad(B, ((0, m - B.shape[0]), (0, m - B.shape[1])), mode='constant')
 
    # Perform Strassen's algorithm on matrices A and B
    C = strassen(A, B)
 
    # Print the resulting matrix
    print(C[:2, :2])
A = []
archivoA = open("A2000.txt", 'r')
for linea in archivoA:
    fila = list(map(int, linea.split()))
    A.append(fila) 
B = []
archivoB = open("B2000.txt", 'r')
for linea in archivoB:
    fila = list(map(int, linea.split()))
    B.append(fila)
archivoB.close()
archivoA.close()

inicio = time.time()
 
main(A,B)
final = time.time() 
print(final -inicio)
