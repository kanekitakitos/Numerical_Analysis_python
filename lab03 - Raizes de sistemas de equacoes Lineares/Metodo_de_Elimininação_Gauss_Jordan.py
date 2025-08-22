from sympy import *

## A característica (posto) de A, denotada car(A), é o número de linhas não nulas de A na sua forma de escada (escalonada).
## Se car(A) = n (onde n é o número de incógnitas), e o sistema for possível, ele será determinado.

# Sistema AX = B, onde [A|B] representa a matriz ampliada (correspondência de A e B)
# Classificação do sistema:
# - Sistema Possível e Determinado: car(A) = car(A|B) = n
# - Sistema Possível e Indeterminado: car(A) = car(A|B) < n
# - Sistema Impossível: car(A) != car(A|B)
#
# A = matriz dos coeficientes
# B = matriz dos resultados (termos independentes)
# Retorna a matriz com os valores de X
# https://github.com/sympy/sympy/blob/d293133e81194adc11177729af91c970f092a6e7/sympy/matrices/solvers.py#L437


# Função para verificar se o determinante é zero
# Se o determinante é zero, o sistema pode ainda ser possível e indeterminado (infinitas soluções),
# ou impossível (sem solução), dependendo das características.
# Se det(A) != 0, o sistema é sempre possível e determinado (SPD).
def is_determinante_zero(matrix: Matrix):
    return matrix.det() == 0



# Função para calcular a característica de uma matriz
def calcula_caracteristica(A: Matrix, B:Matrix):
    # Calcular as características de A e da matriz ampliada A|B
    car_A = A.rank()  # Característica da matriz A
    A_ampliada = A.row_join(B)  # Matriz ampliada [A|B]
    car_A_B = A_ampliada.rank()  # Característica da matriz ampliada

    # Número de incógnitas. É sabido através do número de colunas da matriz A
    n = A.cols

    if car_A == car_A_B == n:
        print("\nO sistema é possível e determinado: solução única.")
        return true
    # Sistema possível e indeterminado ou impossível
    elif (car_A == car_A_B) and (car_A < n):
        # Sistema possível e indeterminado
        print("\nO sistema é possível e indeterminado: infinitas soluções.")
        return false
    elif car_A != car_A_B:
        # Sistema impossível
        print("\nO sistema é impossível: a característica de A difere da característica de A|B.")
        return false
    else:
        # nunca deverá printar isto
        print("\nO Derminante é zero, mas nao é possivel indeterminado ou impossivel, algo de errado aconteceu......")
        return false



# Método de Gauss-Jordan com classificação do sistema
def metodo_Gauss_Jordan(A: Matrix, B: Matrix):

        A_ampliada = A.row_join(B)  # Matriz ampliada [A|B]
        print("---> Matriz A|B: ")
        pprint(A_ampliada)

        # Classificação do sistema
        if is_determinante_zero(A) is not true and calcula_caracteristica(A,B):
            # Sistema possível e determinado (Double Check, e reduntante, pois sabe-se que se determinante != 0, o sistema é SPD)
            sol, _ = A.gauss_jordan_solve(B)
            return sol
        else:
            return "O determinante é diferente de zero e nao é possivel determinado, algo de errado aconteceu......"

