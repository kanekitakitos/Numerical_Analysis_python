# REGRAS PARA COMPREENDER O CODIGO
# xi = x0 + i*h
# x0 = a + h
# xn = b − h
# h = (b − a)/(n + 2)
# x(−1) = a
# x(n+1) = b

# n = 0
# precisa de 3 pontos n+2
# Fórmula: ∫f(x)dx ≈ 2h * f(x0)
def regra_do_ponto_medio(funcao_ou_Pontos, intervalo:tuple):
    """
    Calcula a integral usando a regra do ponto médio.

    @param funcao_ou_Pontos A função ou lista de pontos a serem integrados.
    @param intervalo O intervalo de integração (a, b).
    @return O valor da integral calculada.
    """
    a, b = intervalo
    h = (b-a)/2
    x0 = a + h
    if not isinstance(funcao_ou_Pontos, list) :
        funcao = funcao_ou_Pontos
        valor_final = 2*h*funcao.subs("x",x0)

        return valor_final.n()
    else:
        if len(funcao_ou_Pontos) < 1: raise ValueError("Precisa de minimo 1 (Pontos) sem contar com os pontos dos extremos")
        ponto0 = funcao_ou_Pontos[1]
        valor_final = 2*h*ponto0.y

        return valor_final.n()


# n = 1
# precisa de 4 pontos n+2
# Fórmula: ∫f(x)dx ≈ (3h/2) * [f(x0) + f(x1)]
def regra_do_grau_1(funcao_ou_Pontos , intervalo:tuple):
    """
    Calcula a integral usando a regra do grau 1.

    @param funcao_ou_Pontos A função ou lista de pontos a serem integrados.
    @param intervalo O intervalo de integração (a, b).
    @return O valor da integral calculada.
    """
    a, b = intervalo
    h = (b-a)/3

    if not isinstance(funcao_ou_Pontos, list) :
        funcao = funcao_ou_Pontos
        x0 = a + h
        x1 = a + 2*h

        valor_final = 3*h/2 *(funcao.subs("x",x0) + funcao.subs("x",x1) )
        return valor_final.n()

    else:
        if len(funcao_ou_Pontos) < 2: raise ValueError("Precisa de minimo 2 (Pontos) sem contar com os pontos dos extremos")

        ponto0, ponto1 = funcao_ou_Pontos[0], funcao_ou_Pontos[1]
        valor_final = 3*h/2*(ponto0.y + ponto1.y)
        return valor_final.n()

# n = 2
# precisa de 5 pontos n+2
# Fórmula: ∫f(x)dx ≈ (4h/3) * [2f(x0) - f(x1) + 2f(x2)]
def regra_de_Milne(funcao_ou_Pontos , intervalo:tuple):
    """
    Calcula a integral usando a regra de Milne.

    @param funcao_ou_Pontos A função ou lista de pontos a serem integrados.
    @param intervalo O intervalo de integração (a, b).
    @return O valor da integral calculada.
    """
    a, b = intervalo
    h = (b-a)/4
    if not isinstance(funcao_ou_Pontos, list) :
        funcao = funcao_ou_Pontos
        x0 = a + h
        x1 = a + 2*h
        x2 = a + 3*h

        valor_final = 4*h/3*(2*funcao.subs("x",x0) - funcao.subs("x",x1) + 2*funcao.subs("x",x2))

        return valor_final.n()

    else:
        if len(funcao_ou_Pontos) < 3: raise ValueError("Precisa de minimo 3 (Pontos) sem contar com os pontos dos extremos")

        ponto0, ponto1, ponto2 = funcao_ou_Pontos[0], funcao_ou_Pontos[1], funcao_ou_Pontos[2]
        valor_final = 4*h/3*(2*ponto0.y - ponto1.y + 2*ponto2.y)

        return valor_final.n()

# n = 3
# precisa de 6 pontos n+2
# Fórmula: ∫f(x)dx ≈ (5h/24) * [11f(x0) + f(x1) + f(x2) + 11f(x3)]
def regra_do_grau_3(funcao_ou_Pontos, intervalo:tuple):
    """
    Calcula a integral usando a regra do grau 3.

    @param funcao_ou_Pontos A função ou lista de pontos a serem integrados.
    @param intervalo O intervalo de integração (a, b).
    @return O valor da integral calculada.
    """
    a, b = intervalo
    h = (b-a)/5
    if not isinstance(funcao_ou_Pontos, list) :
        funcao = funcao_ou_Pontos
        x0 = a + h
        x1 = a + 2*h
        x2 = a + 3*h
        x3 = a + 4*h

        valor_final = 5*h/24*(11*funcao.subs("x",x0) + funcao.subs("x",x1) + funcao.subs("x",x2) + 11*funcao.subs("x",x3) )

        return valor_final.n()

    else:
        if len(funcao_ou_Pontos) < 4: raise ValueError("Precisa de minimo 4 (Pontos) sem contar com os pontos dos extremos")

        ponto0, ponto1, ponto2, ponto3 = funcao_ou_Pontos[0], funcao_ou_Pontos[1], funcao_ou_Pontos[2], funcao_ou_Pontos[3]
        valor_final = 5*h/24*(11*ponto0.y + ponto1.y + ponto2.y + 11*ponto3.y)

        return valor_final.n()

#---------------------------------------------------------------------------------------------------------------


class Newton_Cotes_Abertas:
    """
    Classe para calcular integrais usando as regras de Newton-Cotes Abertas.

    @param funcao_ou_Pontos A função ou lista de pontos a serem integrados.
    @param intervalo O intervalo de integração (a, b).
    @param round_number O número de casas decimais para arredondar o resultado.
    """

    def __init__(self, funcao_ou_Pontos, intervalo:tuple):
        self.funcao_ou_Pontos = funcao_ou_Pontos
        self.intervalo = intervalo

        self.todos_os_metodos = \
            {
                0: regra_do_ponto_medio,
                1: regra_do_grau_1,
                2: regra_de_Milne,
                3: regra_do_grau_3,
            }


    def metodo(self, n):
        """
        Seleciona e aplica o método de integração baseado no valor de n.

        @param n O índice do método de integração a ser usado (0 a 3).
        @return O valor da integral calculada ou uma mensagem de erro se n for inválido.
        """
        if n < 0 or n > 3:
            return "Escolha um método válido"

        return self.todos_os_metodos[n](self.funcao_ou_Pontos, self.intervalo)
