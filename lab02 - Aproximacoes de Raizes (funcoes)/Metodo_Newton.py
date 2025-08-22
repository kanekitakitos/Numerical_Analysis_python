from sympy import *
from Metodo_Bissecao import teorema_bolzano

ITERACOES_E_ERROS_NEWTON = 10 , 10**-100

# Formula de Newton. Não é utilizado no codigo, é apenas ilustrativo
FORMULA_NEWTON = "x - f(x)/f'(x)"

# Verificar se o extremo é favorável
# significa que o sinal ( + ou -) na funçao e na segunda derivada, deve ser igual
def extremo_favoravel(equacao:symbols, a):
    ponto_a = equacao.subs('x', a)
    ponto_a_segunda_derivada = diff(diff(equacao, 'x'), 'x').subs('x', a)

    return ponto_a*ponto_a_segunda_derivada > 0

# Escolher ponto favorável do intervalo
# ajuda a encontrar o ponto inicial para o método de Newton
# para convergir mais rapidamente
def escolher_ponto_favoravel(eq:symbols, intervalo:tuple):
    a , b = intervalo
    if extremo_favoravel(eq, a):
        return a
    elif extremo_favoravel(eq, b):
        return b
    else:# se nenhum dos extremos for favorável, escolher o ponto médio
        return (a+b)/2
    

# Método de Newton
# O método de Newton é um método iterativo para encontrar raízes de uma função
# real. Ele usa a ideia de aproximar a função por uma reta tangente e estimar
# a raiz da equação da reta tangente.
def metodo_de_newton(equacao:symbols, intervalo:tuple , iteracoes_erro:tuple):

        if not teorema_bolzano(equacao, intervalo):
            return "Não existe zero no intervalo ou existe mais do que um zero pelo teorema de Bolzano"

        numero_de_iteracoes, tolerancia_de_erro = iteracoes_erro
        primeira_derivada = diff(equacao, 'x')
        k = 1

        #Pedir aproximação inicial
        aprx_ini = escolher_ponto_favoravel(equacao, intervalo)
        r = 0 # raiz ou aproximacao da raiz
        print("-----------------------------")
        print(f'Aproximação Dada: {aprx_ini}')

        while k <= numero_de_iteracoes:
            r = aprx_ini - equacao.subs('x', aprx_ini) / primeira_derivada.subs('x', aprx_ini) # Calculo do Rk
            print(f'\t {k}a aproximação: {float(r)}')
            if abs(r - aprx_ini) < tolerancia_de_erro:
                print(f"\t\tEncontrámos raiz! <- SUCESSO")
                return r
            k += 1
            aprx_ini = r

        return f"Atingimos o número máximo de {numero_de_iteracoes} iterações sem encontrar a raiz com a tolerância especificada."

