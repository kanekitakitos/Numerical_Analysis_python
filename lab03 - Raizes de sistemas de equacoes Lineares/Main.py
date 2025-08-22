from sympy import *
from Metodo_de_Elimininação_Gauss_Jordan import  metodo_Gauss_Jordan
from Metodo_de_Gauss_Seidel import metodo_Gauss_Seidel ,aproximacoes_iteracoes_gauss_seidel
from Metodo_de_Jacobi import metodo_Jacobi, aproximacoes_iteracoes_jacobi

def _prompt_todas_iteracoes(function, resposta_do_metodo):
    if function == metodo_Jacobi:
        iteracoes = aproximacoes_iteracoes_jacobi
    elif function == metodo_Gauss_Seidel:
        iteracoes = aproximacoes_iteracoes_gauss_seidel

    print("------------------------------------------------------------------------------------")
    print("\nTodas as aproximações (em valores decimais):\n--->| X₀ | X₁ | X₂ | ... | Xₙ |\n")
    for idx, aprox in enumerate(iteracoes):
        print(f"Iteração {idx}: {aprox}")

    print("\nSolução aproximada: ", resposta_do_metodo.evalf())
    print("------------------------------------------------------------------------------------")

def prompt_ver_iteracoes_do_metodo(function, resposta_do_metodo):
    resposta = (input("Deseja ver todas as iterações do método? (Y/N) \n"))
    if resposta == "Y" or resposta == "y":
        _prompt_todas_iteracoes(function, resposta_do_metodo)
    else:
        print("Ordem da aproximação: | X₀ | X₁ | X₂ | ... | Xₙ |")
        print("Solução aproximada: ", resposta_do_metodo.evalf())
        print("------------------------------------------------------------------------------------")
#---------------------------------------------------------------------------------------------

# transforma a string em float
# Exemplo: "1 2 3" -> [1.0, 2.0, 3.0]
def string_to_float(string):
    linha = string.split(" ")
    linha = [float(i) for i in linha]
    return linha

# Pega a matriz A e B do usuário
# deve ser uma matriz quadrada e uma matriz vertical
# limite de 3x3
def get_matrix():
    A , B = Matrix(), Matrix()
    n = int(input("Digite o numero de linhas/clunas da matriz (Quadrada): \n"))

    print("Digite as linhas da matriz A (Quadrada):")
    for i in range (0, n):
            linha = string_to_float(input())
            A = A.row_insert(i, Matrix([linha]))

    linha = input("Digite a linha da matriz B (Vertical): \n")
    linha = string_to_float(linha)
    B = Matrix(linha) # adiciona verticalmente

    return A,B


def Main():
    try:
        matriz_A , matriz_B = get_matrix()
        print('1) Metodo de Gauss Jordan \n2) Metodo de Jacobi \n3) Metodo de Gauss Seidel')
        metodo = int(input("Qual o método que deseja aplicar? \n"))

        if metodo == 1:
            aproximacao = metodo_Gauss_Jordan(matriz_A, matriz_B)
            pprint(aproximacao)

        elif metodo == 2:
            aproximacao = metodo_Jacobi(matriz_A, matriz_B)
            prompt_ver_iteracoes_do_metodo(metodo_Jacobi, aproximacao)

        elif metodo == 3:
            aproximacao = metodo_Gauss_Seidel(matriz_A, matriz_B)
            prompt_ver_iteracoes_do_metodo(metodo_Gauss_Seidel, aproximacao)
    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    Main()