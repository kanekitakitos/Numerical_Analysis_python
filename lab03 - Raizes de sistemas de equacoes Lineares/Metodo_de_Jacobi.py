from Metodo_de_Elimininação_Gauss_Jordan import is_determinante_zero
from sympy import *
FORMULA = "Xᵏ= D⁻¹*(L+U)* Xᵏ⁻¹ + D⁻¹*B" # ou  Xᵏ⁺¹= D⁻¹ * (L+U) * X(k) + D⁻¹ * B
ITERACOES_ERRO = 10, 10**-4

aproximacoes_iteracoes_jacobi = []

def prompt_is_not_diagonalmente_dominante():
    resposta = input("Deseja continuar? (Y/N)")
    if resposta == "y" or resposta == "Y":
       return 1
    else:
       return 0

#-------------------------------------------------------------------------------------------
# Python function to check whether the given matrix is Diagonally Dominant Matrix.
# Code by manishshaw1, @GeeksforGeeks, presented to us by HBO.
# Code suffered changes to become fully compatible with the sympy library.
def isDDM(m:Matrix):

    n = m.rows # number of rows
    # for each row
    for i in range(0, n):
        # for each column, finding sum of each row.
        sum = 0
        for j in range(0, n):
            sum += abs(m[i,j])
        # removing the diagonal element.
        sum -= abs(m[i,i])

        # checking if diagonal element is less than sum of non-diagonal elements.
        if abs(m[i,i]) < sum:
            return False
    return True

# Calcula a primeira iteracao do metodo de Jacobi seguindo a formula
# Retorna T, C e X₀ (primeira iteracao)
def primeira_iteracao(A: Matrix, B: Matrix):
    D = diag(*A.diagonal())  # STEP 1, DIVIDE A EM "D", "L" e 'U'
    L = A.lower_triangular() - D
    U = A.upper_triangular() - D
    D_inv = D.inv()  # STEP 2, CALCULA D⁻¹
    T = -D_inv * (L + U)  # STEP 3, CALCULA T
    C = D_inv * B  # STEP 4, CALCULA C
    X_0 = Matrix([0,0,0])  # STEP 5, CALCULA X₀, primeira iteracao do valor X₀

    return T, C, X_0

# Calcula os valores iniciais da primeira iteracao do metodo de Jacobi
# X₀ = SOMATORIO (b(i)/a(i,i))
# Retorna uma matriz com os valores iniciais
def get_X0_primeira_iteracao(D: Matrix, B: Matrix):
    x_0 = []
    for i in range(0, B.shape[0]):
        x_0.append(B[i, 0] / D[i, i])

    return Matrix(x_0).reshape(B.shape[0], 1) # Retorna uma matriz coluna


def get_max(A , B):
    max = 0.0
    current = 0.0
    for i in range(0, A.shape[0]):
        current = abs(A[i,0] - B[i,0])
        if current > max :
            max = current
    return max


# Calcula o método de Jacobi
# A = matriz dos coeficientes
# B = matriz dos resultados
# Retorna a matriz com os valores aproximados de X
def metodo_Jacobi(A: Matrix, B: Matrix):
    if is_determinante_zero(A):
        raise Exception("Determinante da matriz é zero, sistema não pode ser resolvido.")

    if not isDDM(A):
        print("A matriz não é diagonalmente dominante, o método de Jacobi pode não convergir.")
        if prompt_is_not_diagonalmente_dominante() == 0:
            return

    # Se a matriz for diagonalmente dominante ou o utilizador decidir continuar
    iteracoes, erro = ITERACOES_ERRO

    T, C, X_anterior = primeira_iteracao(A, B)
    X_proximo = None

    aproximacoes_iteracoes_jacobi.append([float(x) for x in X_anterior])

    for i in range(1, iteracoes + 1):
        X_proximo = T * X_anterior + C

        aproximacoes_iteracoes_jacobi.append([float(x) for x in X_proximo])

        # Critério de parada
        if get_max(X_proximo, X_anterior) < erro:
            print(f"Convergiu na iteração {i}")
            return X_proximo

        X_anterior = X_proximo

    # Caso não tenha convergido, imprimir a última aproximação encontrada
    print("Número máximo de iterações excedido. Procedimento concluído sem sucesso.")
    return X_proximo


