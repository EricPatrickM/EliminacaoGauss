#include <iostream>
#include <stdio.h>
#include <stdlib.h>


/*float detLaplace(int n, float a)
{
    if (n == 1)
    {
        // Caso base: matriz 1x1
        return a[0][0];
    }
    else
    {
        float det = 0;
        int i, row, col, j_aux, i_aux;

        // Escolhe a primeira linha para calcular os cofatores
        for (i = 0; i < n; i++)
        {
            // ignora os zeros (zero vezes qualquer número é igual zero)
            if (a[0][i] != 0)
            {
                float aux[n - 1][n - 1];
                i_aux = 0;
                j_aux = 0;
                // Gera as matrizes para calcular os cofatores
                for (row = 1; row < n; row++)
                {
                    for (col = 0; col < n; col++)
                    {
                        if (col != i)
                        {
                            aux[i_aux][j_aux] = a[row][col];
                            j_aux++;
                        }
                    }
                    i_aux++;
                    j_aux = 0;
                }
                float factor = (i % 2 == 0) ? a[0][i] : -a[0][i];
                det = det + factor * detLaplace(n - 1, aux);
            }
        }
        return det;
    }
}*/

/*void comutar(float *a, int n){

}
*/
int main()
{   
    int n = 3;
    float m, x[n], soma = 0;
    float matriz[n][n + 1] = {{3, -2, 5, 20}, {6, -9, 12, 51}, {-5, 0, 2, 1}};
    float matrizlaplace[n][n];

    //comutar((int *)a, n);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            matrizlaplace[i][j] = matriz[i][j];
        }
    }

   // if (detLaplace(n, matrizlaplace) != 0)
    //{
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n + 1; j++)
            {
                printf("%f |", matriz[i][j]);
            }
            printf("\n");
        }
        printf("passo 1 \n");
        for (int i = 0; i < n; i++)
        {
            printf("passo 2 \n");
            for (int j = 0; j < n; j++)
            {
                if (j > i)
                {
                    printf("passo 3 \n");
                    m = -1 * (matriz[j][i] / matriz[i][i]);
                    for (int k = 0; k < n + 1; k++)
                    {
                        matriz[j][k] = m * matriz[i][k] + matriz[j][k];
                    }
                }
            }
        }
        printf("passo 2");
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n + 1; j++)
            {
                printf("%f |", matriz[i][j]);
            }
            x[i] = 1;
            printf("\n");
        }

        for (int i = n - 1; i >= 0; i--)
        {
            soma = 0;
            for (int j = i + 1; j < n; j++)
            {
                soma += x[j] * matriz[i][j];
            }
            x[i] = (matriz[i][n] - soma) / matriz[i][i];
        }

        for (int i = 0; i < n; i++)
        {
            printf("\nx%d=%f\t", i, x[i]);
        }
    //} else {
        //printf("Matriz Invalida");
    //}
    return 0;
}