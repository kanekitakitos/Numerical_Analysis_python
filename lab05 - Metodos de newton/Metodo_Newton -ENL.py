import numpy as np
import sympy as sp




def read_input():
#----------------------------------------------------------------------------------------
    # Ler o número de equações/variáveis
    n = int(input("Digite o número de equações/variáveis: "))
    # Criar as variáveis simbólicas x1, x2, ..., x{n}, que o simpy vai reconhecer como variáveis reais
    vars = sp.symbols(' '.join([f'x{i}' for i in range(1, n + 1)]), real=True)

    # Criar um dicionário local que inclua as funções e as variáveis
    # este local dict inclui as funções seno, cosseno, exponencial e pi, além das variáveis x1, x2, ..., x{n}
    # quando formos escrever as equações, podemos usar sin(x1), cos(x2), etc.
    # alem de poder usar x1, x2, ..., x{n} diretamente
    # NAO PODEMOS, no entanto, usar nada alem de x1, x2, ..., x{n} como variáveis, ex: y, z, etc.
    local_dict = {
                  "sin": sp.sin, "cos": sp.cos, "exp": sp.exp, "pi": sp.pi, "tan": sp.tan, "sqrt": sp.sqrt, "log": sp.log,
                  "abs": sp.Abs, "ln": sp.ln, "e": sp.exp,"^" : "**" , "sen": sp.sin , "π": sp.pi, "ℯ": sp.exp(1)
                 }
    for i, var in enumerate(vars, start=1):
        local_dict[f"x{i}"] = var  # associa 'x1' -> vars[0], 'x2' -> vars[1], etc.

#----------------------------------------------------------------------------------------
    # Matriz F ->
    # Matriz que contém as equações que queremos resolver, isto é
    # F[0] = f1(x1, x2, ..., x{n})
    # F[1] = f2(x1, x2, ..., x{n})
    # etc

    F = []
    print(f"Digite {n} equações, uma por linha, em função de x1, x2, ..., x{n}:")
    for i in range(n):
        eq_str = input(f"Equação {i + 1}: ")
        eq_sym = sp.sympify(eq_str, locals=local_dict)  # usa o local_dict com as variáveis corretas
        F.append(eq_sym)

#----------------------------------------------------------------------------------------
    # Aproximação inicial x0 ->
    x0_str = input(f"Digite a aproximação inicial (vetor de {n} valores) separados por espaço: ")
    # Converte a string de valores separados por espaço em um array de floats
    x0 = np.array([float(val) for val in x0_str.split()])

    # Tolerância e número máximo de iterações ->
    tol = float(sp.sympify(input("Digite a tolerância absoluta (norma infinito), ex: 0.0001: ")))
    max_iter = int(input("Digite o número máximo de iterações: "))

#----------------------------------------------------------------------------------------


    print("----------------------------------------------------------------------------------------")
    # A leitura do input retorna as variáveis, as equações, a aproximação inicial, a tolerância e o número máximo de iterações
    return vars, F, x0, tol, max_iter


#-----------------------------------------------------------------------------------------------------------------




def get_matriz_jacobiana(vars, F):
    """
     Função que gera a matriz Jacobiana.
     A matriz Jacobiana é uma matriz de derivadas parciais de cada equação em relação a cada variável.
    Lembrando que derivada parcial em relação a x1 é representada por diff(f, x1), ou seja, as restantes variaveis sao consideradas constantes.
    """

    n = len(F)
    J = sp.zeros(n, n)
    for i, f in enumerate(F): # para cada equação do sistema
        for j, var in enumerate(vars): # para cada variável (de cada equação do sistema)
            J[i, j] = sp.diff(f, var) # a expressao da derivada parcial de f em relação a var, usando a funcao do sympy
    return J


def F_eval(F_funcs, x):
    """
    F_eval
    Calcula o valor de cada equação do sistema no ponto x, retornando um array com os resultados
    """

    return np.array([f(*x) for f in F_funcs], dtype=float)


def J_eval(J_funcs, x):
    """
    J_eval
    Calcula o valor de cada derivada parcial de cada equação do sistema no ponto x, retornando uma matriz com os resultados
    """

    n = len(J_funcs)
    J_val = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            J_val[i, j] = J_funcs[i][j](*x)
    return J_val


def cria_funcoes_numericas(vars, F, J):

#     Usando as variáveis, as equações definidas e a matriz Jacobiana calculada:
#     Criamos funções numéricas para evitar o cálculo repetido de derivadas e valores de funções simbólicas.
#     Isso é feito com `lambdify`, que transforma expressões simbólicas em funções Python otimizadas para
#     cálculos numéricos.

#     Por exemplo, resolver simbolicamente requer `f.subs(x1, x[0]).subs(x2, x[1])...` seguido de `f.evalf()`.
#     Com `lambdify`, basta fazer `f(*x)` diretamente, onde `x` é o vetor de valores para as variáveis, e
#     o valor numérico da função é retornado.

#     !!!!!!!! Importante !!!!!!!!!:
#     - `F_funcs` é uma lista de funções numéricas que representam as equações de F(x).
#     - Para calcular o valor da i-ésima equação em um ponto x, usa-se `F_funcs[i](*x)`.
#     - Para calcular o vetor \( F(x) \) completo, faz-se:
#           `F_valores = np.array([f(*x) for f in F_funcs], dtype=float)`
#     - `J_funcs` é uma matriz (lista de listas) de funções numéricas que representam as derivadas parciais de J(x).
#     - Para calcular o valor da derivada parcial \ ( J[i][j] \ ) em um ponto x, usa-se `J_funcs[i][j](*x)`.
#     - Para calcular toda a matriz Jacobiana \( J(x) \), pode-se preencher uma matriz com:
#           `J_valores = np.array([[J_funcs[i][j](*x) for j in range(n)] for i in range(n)], dtype=float)`



    F_funcs = [sp.lambdify(vars, f, "numpy") for f in F]
    n = len(F)
    J_funcs = [[sp.lambdify(vars, J[i, j], "numpy") for j in range(n)] for i in range(n)]
    return F_funcs, J_funcs


def metodo_de_Newton(F_funcs, J_funcs, x0, tol, max_iter):

    """
     Metodo de Newton propriamente dito.
     Recebe as funções numéricas de F(x) e J(x), a aproximação inicial x0, a tolerância e o número máximo de iterações.
    """

    x = np.array(x0, dtype=float) # x é a aproximação inicial separada com espaço, mas convertida para um array de floats

    x_results = []

    for k_iteracoes in range(1, max_iter + 1):
        Fx = F_eval(F_funcs, x)             # Fx é o vetor de valores das equações no ponto x
        Jx = J_eval(J_funcs, x)             # Jx é a matriz Jacobiana no ponto x

        x_results.append(x)

        try:
            y = np.linalg.solve(Jx, -Fx)

        except np.linalg.LinAlgError:
            print("A matriz Jacobiana é singular. Não foi possível avançar.")
            return x, k_iteracoes, False

        print(f"Iteração {k_iteracoes}:")
        print("x =", x)

        x_new = x + y
        if np.linalg.norm(y, ord=np.inf) < tol:
            return x_results, x_new, k_iteracoes, True

        x = x_new

    return x_results, x, max_iter, False



#---------------------- MAIN --------------- MAIN ------------------- MAIN ------------------------------ MAIN --------------- MAIN ------------

def main():
    while True:
        print()
        vars, F, x0, tol, max_iter = read_input()

        print("\nVariáveis:", vars)
        print("Equações:")
        for eq in F:
            print(eq)
        print("----------------------------------------------------------------------------------------")
        J = get_matriz_jacobiana(vars, F)

        F_funcs, J_funcs = cria_funcoes_numericas(vars, F, J)
        results, sol, k, success = metodo_de_Newton(F_funcs, J_funcs, x0, tol, max_iter)

        if success:
            print(f"Convergiu em {k} iterações.")
            print("  Solução aproximada ---> ", sol)
        else:
            print("Não convergiu no número máximo de iterações.")
            print("  Última aproximação --->", sol)
        print()
        print("----------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
