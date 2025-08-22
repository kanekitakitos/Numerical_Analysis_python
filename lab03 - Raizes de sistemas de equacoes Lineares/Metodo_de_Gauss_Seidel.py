from Metodo_de_Elimininação_Gauss_Jordan import is_determinante_zero
from sympy import *
from Metodo_de_Jacobi import prompt_is_not_diagonalmente_dominante, get_X0_primeira_iteracao, isDDM , get_max
FORMULA = "Xᵏ= D⁻¹*B -D⁻¹*U*Xᵏ - D⁻¹*L*Xᵏ⁻¹ "# ou Xᵏ⁺¹ = D⁻¹* B -D⁻¹*U*Xᵏ⁺¹ - D⁻¹* L*Xᵏ "
ITERACOES_ERRO = 10, 10**-4

# Lista para armazenar todas as iterações
aproximacoes_iteracoes_gauss_seidel = []

# Calcula a proxima iteracao do metodo de Gauss-Seidel
# LOGICA:
#   Conhecendo o valor inicial de X (X₀), calculamos o próximo valor de X,
#   utilizando o valor anterior. Após cada cálculo, atualizamos o valor de
#   X na matriz correspondente. Assim, em cada iteração, utilizamos o valor
#   mais recente de X
# Retorna a matriz com os valores aproximados de X
def proxima_iteracao(A: Matrix, B: Matrix, X: Matrix):
    n = A.shape[0]
    x_novo = 0.0
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                x_novo += (B[j, 0])
            elif i != j:
                x_novo += A[i, j] * X[j, 0] * -1
        X[i, 0] = x_novo * (1 / A[i, i])
        x_novo = 0.0

    return X

def getMaxIndex(matrix: Matrix):
    max = 0
    index = 0
    for i in range(0, matrix.shape[0]):
        if matrix[i, 0] > max:
            max = matrix[i, 0]
            index = i
    return index

# descobre o indice com o valor maximo da matriz X1 e faz a subtração de X2 no indice index, e de X1 no indice index
def getErro(X1: Matrix, X2: Matrix):
    index = getMaxIndex(X1)
    return abs(X1[index, 0] - X2[index, 0])


# Calcula o metodo de Gauss-Seidel
# processo parecido com o de jacobi só com uma convergencia mais rapida
# A = matriz dos coeficientes
# B = matriz dos resultados
# Retorna a matriz com os valores aproximados de X
def metodo_Gauss_Seidel(A: Matrix, B: Matrix):
    if is_determinante_zero(A):
        raise Exception("Determinante da matriz é zero, sistema não pode ser resolvido.")

    if not isDDM(A):
        print("A matriz não é diagonalmente dominante, o método de Jacobi pode não convergir.")
        if prompt_is_not_diagonalmente_dominante() == 0:
            return

    # Se a matriz for diagonalmente dominante ou o utilizador decidir continuar
    iteracoes, erro = ITERACOES_ERRO

    X_0 = get_X0_primeira_iteracao(A, B)  # X₀, primeira iteração do valor X₀
    X_anterior = X_0.copy()  # Inicializa X_anterior com X₀
    aproximacoes_iteracoes_gauss_seidel.append([float(x) for x in X_0])  # Armazena X₀

    for i in range(iteracoes):
        X_proximo = proxima_iteracao(A, B, X_anterior.copy())  # Calcula Xᵏ⁺¹
        aproximacoes_iteracoes_gauss_seidel.append([float(x) for x in X_proximo])  # Armazena a nova aproximação

        # Critério de paragem com norma infinita
        diferencas = (X_proximo - X_anterior).applyfunc(abs)  # Diferenças absolutas
        norma_infinita = max([diferencas[j, 0] for j in range(diferencas.rows)])  # Máximo das diferenças

        if norma_infinita < erro:
            print(f"Convergiu na iteração {i + 1}")  # Imprime a iteração correta
            return X_proximo

        X_anterior = X_proximo.copy()  # Atualiza X_anterior

    # Caso não tenha convergido, imprimir a última aproximação encontrada
    print("Número máximo de iterações excedido. Procedimento concluído sem sucesso.")
    return X_proximo
