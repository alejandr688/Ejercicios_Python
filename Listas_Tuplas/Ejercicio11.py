A = [[1, 2, 3],
     [4, 5, 6]]

B = [[-1, 0],
     [0, 1],
     [1, 1]]


#Primero creas una matriz de ceros de 2x2


resultado=[[0 for j in range(2)] for i in range(2)]
print(resultado)

#Ahora haces la multiplicación de matrices

for i in range(2):
    for j in range(2):
        for k in range(3):
            resultado[i][j]+=A[i][k]*B[k][j]
            
print(resultado)
for fila in resultado:
    print(fila)