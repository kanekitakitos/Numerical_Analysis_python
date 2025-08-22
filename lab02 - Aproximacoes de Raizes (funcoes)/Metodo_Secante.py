from sympy import *
from Metodo_Bissecao import teorema_bolzano

ITERACOES_E_ERROS_SECANTE = 10 , 10**-1

# Formula da secante. Não é utilizado no codigo, é apenas ilustrativo
FORMULA = 'rn =  rn-1 - (f(rn-1) * (rn-1 - rn-2)) / (f(rn-1) - f(rn-2))'


def metodo_da_secante(equacao:symbols, intervalo, iteracoes_erro:tuple):

    if not teorema_bolzano(equacao, intervalo):
        return "Não existe zero no intervalo ou existe mais do que um zero pelo teorema de Bolzano"

    a, b = intervalo #r0 e r1
    numero_de_iteracoes, tolerancia_de_erro = iteracoes_erro # No e Tol

    k = 2 # Contador de iterações
    y0 = equacao.subs('x', a)
    y1 = equacao.subs('x', b)

    r = 0 # raiz ou aproximacao da raiz

    print(f"Intervalo / Aproximações iniciais: {a} , {b}")


    while k <= numero_de_iteracoes:
        r = b - (y1 * (b - a)) / (y1 - y0) # Calculo do Rk
        print(f'----------------------------------------------')
        print(f'\t {k}a aproximação: {float(r)}')
        if abs(r - b) < tolerancia_de_erro:
            print(f"\t\tEncontrámos raiz! <- SUCESSO")
            return r #Deu certo
        k+=1
        a = b
        y0 = y1
        b = r
        y1 = equacao.subs('x', r)

    return f"Atingimos o número máximo de {numero_de_iteracoes} iterações sem encontrar a raiz com a tolerância especificada."