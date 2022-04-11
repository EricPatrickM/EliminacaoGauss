from tkinter import N
import numpy as np

#TamanhoMatriz=3

#POSSIVEL 
TamanhoMatriz=3
#matriz = np.array([[0, -2, 5, 3],[6, 0, 12, 2],[-5, 1, 0, 1]], dtype=float)
#matriz = np.array([[0, -2, 5, 20],[6, -9, 12, 51],[-5, 0, 2, 1]], dtype=float)
#matriz = np.array([[0, -2, 5, 20],[6, -9, 12, 51],[-5, 0, 2, 1]], dtype=float)
#matriz = np.array([[3, -2, 5],[0, 0, 0],[-5, 0, 2]], dtype=float)
#matriz = np.array([[3, -2, 5, 20],[6, -9, 12, 51],[-5, 0, 2, 1]], dtype=float)

# IMPOSSIVEL
#TamanhoMatriz=3
matriz = np.array([[0, -2, 5, 3],[0, 1, 12, 2],[0, 1, 2, 1]], dtype=float)
#matriz = np.array([[0, 0, 5, 20],[0, 0, 12, 51],[0, 0, 2, 1]], dtype=float)
#TamanhoMatriz=3
#matriz = np.array([[1, 2, 1, 0],[2, 1, -3, 0],[3, 3, -2, 0]], dtype=float)
#TamanhoMatriz=3



def zerarTrianguloInferior(matriz, n):
    x=[]
    for i in range(0, n):
        x.append(1)
    print('MATRIZ INICIAL:')
    for i in range(0, n):
        x[i]=1
        for j in range(0, n+1):
            print(str(float(matriz[i][j])) + " | ", end='')
        print()

    for i in range(0,n):
        for j in range(0, n):
            if (j > i):
                m = -1 * (matriz[j][i] / matriz[i][i])
                for k in range(0, n+1):
                    matriz[j][k] = float(m * matriz[i][k] + matriz[j][k])
        comutar(n, matriz, i)

    print('MATRIZ FINAL:')
    for i in range(0, n):
        for j in range(0, n+1):
            print(str(float(matriz[i][j])) + " | ", end='')
        print()

    for i in range(n-1, -1, -1):
            soma = 0
            for j in range(i+1, n):
                soma += x[j] * matriz[i][j];
            x[i] = (matriz[i][n] - soma) / matriz[i][i];

    for i in range(0, n):
        print('x' + str(i) + '=\t' + str(x[i]))


def comutar(n, matriz, linha):
    possui = 0
    print('linha' + str(linha))
    if(matriz[linha][linha]==0):
        for i in range(linha+1,n):
            if(possui == 0 or matriz[linha][i] != 0):
                print('i: ' + str(i))
                for k in range(0, n+1):
                   aux =matriz[linha][k]
                   matriz[linha][k] = matriz[i][k]
                   matriz[i][k] = aux
                possui=1
                break
            #if(possui==1):
                #break
    else:
        for i in range(0, n):
            for j in range(0, n):
                print(str(float(matriz[i][j])) + " | ", end='')
            print()
        return 0


def viabilidadeMetodo(n, matriz):
    matrizlaplace=np.empty([n, n], dtype=float)

    for i in range(0, n):
        for j in range(0, n):
            matrizlaplace[i][j] = matriz[i][j]

    for i in range(0, n):
        for j in range(0, n):
            print(str(float(matrizlaplace[i][j])) + " | ", end='')
        print()

    if(float(np.linalg.det(matrizlaplace))==0):
        print('SISTEMA IMPOSSIVEL')
        print('Determinante: '+ str(float(np.linalg.det(matrizlaplace))))
        return 0
    else:
        print('SISTEMA POSSIVEL')
        print('Determinante: '+ str(float(np.linalg.det(matrizlaplace))))
        return 1

if(viabilidadeMetodo(TamanhoMatriz, matriz)):
    if(matriz[0][0]==0):
        comutar(TamanhoMatriz, matriz, 0)
    zerarTrianguloInferior(matriz, TamanhoMatriz)

