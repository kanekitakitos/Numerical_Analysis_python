#REGRAS PARA COMPREENDER O CODIGO
# xi = x0 + i*h
# i = 0,1 ...... n
# h = (b − a)/n




# n = 1 -> 2 pontos
# Fórmula: ∫f(x)dx ≈ (h/2) * [f(x0) + f(x1)]
def regra_do_Trapezio(funcao_ou_Pontos,  intervalo:tuple):
    """
    Calcula a integral usando a regra do trapézio.

    @param funcao_ou_Pontos A função ou lista de pontos a serem integrados.
    @param intervalo O intervalo de integração (x0, x1).
    @return O valor da integral calculada.
    """
    x0, x1 = intervalo
    h = (x1 - x0)

    if not isinstance(funcao_ou_Pontos, list) :
        funcao = funcao_ou_Pontos
        valor_final = h/2*((funcao.subs("x",x0))+ funcao.subs("x",x1))
        p = (funcao.subs("x", x0))
        p = funcao.subs("x", x1)
        return valor_final.n()

    else:
        if len(funcao_ou_Pontos) < 2: raise ValueError("Precisa de minimo 2 (Pontos)")

        ponto0,ponto1 = funcao_ou_Pontos[0] , funcao_ou_Pontos[1]
        valor_final = h/2*(ponto0.y + ponto1.y)

        return valor_final.n()


# n = 2 -> 3 pontos
# Fórmula: ∫f(x)dx ≈ (h/3) * [f(x0) + 4f(x1) + f(x2)]
def regra_de_Simpson_1(funcao_ou_Pontos , intervalo:tuple):
    """
    Calcula a integral usando a regra de Simpson.

    @param funcao_ou_Pontos A função ou lista de pontos a serem integrados.
    @param intervalo O intervalo de integração (x0, x2).
    @return O valor da integral calculada.
    """
    x0, x2 = intervalo
    x1 = (x0 + x2) / 2
    h = x1 - x0 and x2 - x1 # passo de ponto a ponto uniformemente

    if not isinstance(funcao_ou_Pontos, list) :
        funcao = funcao_ou_Pontos
        valor_final = h/3 *(funcao.subs("x",x0) + 4*funcao.subs("x",x1) + funcao.subs("x",x2))
        return valor_final.n()

    else: # Funciona com pontos
        if len(funcao_ou_Pontos) < 3: raise ValueError("Precisa de minimo 3 (Pontos)")

        ponto0, ponto1, ponto2 = funcao_ou_Pontos[0], funcao_ou_Pontos[1], funcao_ou_Pontos[2]
        h = (ponto2.x - ponto0.x)/2
        valor_final = h/3*(ponto0.y + 4*ponto1.y + ponto2.y)

        return valor_final.n()


# n = 3 -> 4 pontos
# Fórmula: ∫f(x)dx ≈ (3h/8) * [f(x0) + 3f(x1) + 3f(x2) + f(x3)]
def regra_de_Simpson_2(funcao_ou_Pontos , intervalo:tuple):
    """
    Calcula a integral usando a regra de Simpson 3/8.

    @param funcao_ou_Pontos A função ou lista de pontos a serem integrados.
    @param intervalo O intervalo de integração (x0, x3).
    @return O valor da integral calculada.
    """
    x0, x3 = intervalo
    h = (x3 - x0) / 3
    x1 = x0 + h
    x2 = x0 + 2*h

    if not isinstance(funcao_ou_Pontos, list) :
        funcao = funcao_ou_Pontos
        valor_final = 3*h/8*(funcao.subs("x",x0) + 3*funcao.subs("x",x1) + 3*funcao.subs("x",x2) + funcao.subs("x",x3))
        return valor_final.n()

    else: # Funciona com pontos
        if len(funcao_ou_Pontos) < 4: raise ValueError("Precisa de minimo 4 (Pontos)")

        ponto0, ponto1, ponto2, ponto3 = funcao_ou_Pontos[0], funcao_ou_Pontos[1], funcao_ou_Pontos[2], funcao_ou_Pontos[3]
        valor_final = 3*h/8*(ponto0.y + 3*ponto1.y + 3*ponto2.y + ponto3.y)

        return valor_final.n()


# n = 4 -> 5 pontos
# Fórmula: ∫f(x)dx ≈ (2h/45) * [7f(x0) + 32f(x1) + 12f(x2) + 32f(x3) + 7f(x4)]
def regra_de_Boole(funcao_ou_Pontos , intervalo:tuple):
    """
    Calcula a integral usando a regra de Boole.

    @param funcao_ou_Pontos A função ou lista de pontos a serem integrados.
    @param intervalo O intervalo de integração (x0, x4).
    @return O valor da integral calculada.
    """
    x0, x4 = intervalo
    h = (x4 - x0) / 4
    x1 = x0 + h
    x2 = x0 + 2*h
    x3 = x0 + 3*h

    if not isinstance(funcao_ou_Pontos, list) :
        funcao = funcao_ou_Pontos
        valor_final = 2*h/45*(7*funcao.subs("x",x0) + 32*funcao.subs("x",x1) + 12*funcao.subs("x",x2) + 32*funcao.subs("x",x3) + 7*funcao.subs("x",x4))
        return valor_final.n()

    else: # Funciona com pontos
        if len(funcao_ou_Pontos) < 5: raise ValueError("Precisa de minimo 5 (Pontos)")

        ponto0, ponto1, ponto2, ponto3, ponto4 = funcao_ou_Pontos[0], funcao_ou_Pontos[1], funcao_ou_Pontos[2], funcao_ou_Pontos[3], funcao_ou_Pontos[4]
        valor_final = 2*h/45*(7*ponto0.y + 32*ponto1.y + 12*ponto2.y + 32*ponto3.y + 7*ponto4.y)

        return valor_final.n()


class Newton_Cotes_Fechadas:
    """
    Classe para calcular integrais usando as regras de Newton-Cotes Fechadas.

    @param funcao_ou_Pontos A função ou lista de pontos a serem integrados.
    @param intervalo O intervalo de integração (a, b).
    @param round_number O número de casas decimais para arredondar o resultado.
    """

    def __init__(self, funcao_ou_Pontos, intervalo:tuple):
        self.funcao_ou_Pontos = funcao_ou_Pontos
        self.intervalo = intervalo

        self.todos_os_metodos = \
            {
                1: regra_do_Trapezio,
                2: regra_de_Simpson_1,
                3: regra_de_Simpson_2,
                4: regra_de_Boole
            }

    def metodo(self, n):
        """
        Seleciona e aplica o método de integração baseado no valor de n.

        @param n O índice do método de integração a ser usado (1 a 4).
        @return O valor da integral calculada ou uma mensagem de erro se n for inválido.
        """
        if n > 4 or n < 1:
            return "Escolha um metodo valido"

        return self.todos_os_metodos[n](self.funcao_ou_Pontos, self.intervalo)
