# Program to multiply two matrices using list comprehension

# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

# result will be 3x4
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
print(result)