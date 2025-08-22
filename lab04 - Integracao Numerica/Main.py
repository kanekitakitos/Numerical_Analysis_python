from sympy import *
from Newton_Cotes_Fechada import Newton_Cotes_Fechadas
from Newton_Cotes_Aberta import Newton_Cotes_Abertas

ARREDONDAR = 8


# π = '960' valor do caracter
# ℯ = '8495' valor do caracter
def equacao_para_symPy(equacao: str):
    equacao = equacao.replace('^', '**')
    equacao = equacao.replace('sen', 'sin')
    equacao = equacao.replace('tg', 'tan')
    equacao = equacao.replace('e', 'exp(1)')
    equacao = equacao.replace('ℯ', 'exp(1)')
    equacao = equacao.replace('π', 'pi')
    return sympify(equacao)

def equacao_para_string(equacao):
    equacao = str(equacao)
    equacao = equacao.replace('**', '^')
    equacao =equacao.replace('exp(1)', 'e')
    equacao = equacao.replace('pi', 'π')
    return equacao

def intervalo_para_tuple(intervalo:str):
    if ' ' in intervalo :
        intervalo = intervalo.split(' ')
    elif ',' in intervalo:
        intervalo = intervalo.split(',')


    return sympify(equacao_para_symPy(intervalo[0])).n(), sympify(equacao_para_symPy(intervalo[1])).n()

#----------------------------------------------------------------------------------------------------------


def get_Newton_Cote():
    formula = int(input("Qual formulas de Newton Cotes quer usar? \n 1)Newton Cotes-Fechadas \n 2)Newton Cotes-Abertas\n"))
    n = 0
    if formula == 1:
        n = int(input("Qual o grau da formula de Newton Cotes-Fechadas?\n 1)Regra do Trapezio \n 2)Regra de Simpson 1/3 \n 3)Regra de Simpson 3/8\n 4)Regra de Boole\n"))+1
    elif formula == 2:
        n = int(input("Qual o grau da formula de Newton Cotes-Abertas?\n 0)Regra do Ponto Medio \n 1)Regra do Grau 1\n 2)Regra de Milne\n 3)Regra do Grau 3\n"))+1

    print("--------------------------------------------------------------")
    if formula == 1:
        print(f"--> O metodo escolhido precisa de minimo {n} pontos")
    elif formula == 2:
        print(f"--> O metodo escolhido precisa de minimo {n} pontos (tirando os pontos dos extremos)")

    funcao = None
    pontos = []
    funcao_ou_abscissas = str(input("Inserir as Abscissas(separadas com espaço) ou a Função\n")).split(' ')
    if len(funcao_ou_abscissas) > 1:
        x = [float(i) for i in funcao_ou_abscissas]

        funcao_ou_Ordenadas = str(input("Inserir as Ordenadas(separadas com espaço) ou a Função\n")).split(' ')
        if len(funcao_ou_Ordenadas) > 1:
            y = [float(i) for i in funcao_ou_Ordenadas]
            pontos = [Point((x[i], y[i])) for i in range(n)]

        elif len(funcao_ou_Ordenadas) == 1:
            funcao = equacao_para_symPy(funcao_ou_Ordenadas[0])

    elif len(funcao_ou_abscissas) == 1:
        funcao = equacao_para_symPy(funcao_ou_abscissas[0])

    print("--------------------------------------------------------------")
    intervalo = intervalo_para_tuple(input("Inserir o Intervalo de integração\n"))
    print("--------------------------------------------------------------")
    if formula == 2:

        if funcao is None: # se a funcao for None, então a funcao é uma lista de pontos
            funcao = pontos
        return Newton_Cotes_Abertas(funcao, intervalo) , n-1

    elif formula == 1:

        if funcao is None: # se a funcao for None, então a funcao é uma lista de pontos
            funcao = pontos
        return Newton_Cotes_Fechadas(funcao, intervalo) , n-1
    else:
        return "Error metodo não encontrado" , None


#----------------------------------------------------------------------------------------------

def Main():
    try:
        print("--------------------------------------------------------------")
        newton_cote , n = get_Newton_Cote()
        resultado = newton_cote.metodo(n)
        print(f"--> Resultado: {round(resultado,ARREDONDAR)}\n")
        print("--------------------------------------------------------------")


    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    Main()

