from sympy import *

ITERACOES_E_ERROS_BISSECAO = 20 , 10**-5


#  Teorema de Bolzano
#  f(x) uma função contínua em [a,b] e tal que,
#  f(a)*f(b) < 0 então existe pelo menos existe um zero no intervalo [a,b]
#  f(a)*f(b) > 0 não podemos garantir que existe pelo menos um zero no intervalo [a,b]
def teorema_bolzano(equacao:symbols, intervalo:tuple):

    equacao_no_ponto_a = equacao.subs('x', intervalo[0])
    equacao_no_ponto_b = equacao.subs('x', intervalo[1])

    return equacao_no_ponto_a*equacao_no_ponto_b < 0

# Subtituir o valor de x na equação
# e verificar se o sinal é diferente entre os pontos
# se for diferente, então existe pelo menos um zero
# Devolve o ponto onde o sinal é diferente
def get_new_interval(a:float , b:float ,c:float, equacao:symbols):
    if teorema_bolzano(equacao, (a,c))  : #  True se f(a)*f(c) < 0, a e c têm sinais diferentes, logo o zero está entre a e c
        return a , c
    elif teorema_bolzano(equacao, (c,b)): # True se f(c)*f(b) < 0, c e b têm sinais diferentes, logo o zero está entre c e b
        return c , b
    else:
        return None

#  Método da Bisseção
#  O método da bisseção é um método de busca de raízes que divide repetidamente um intervalo ao meio e
#  então seleciona um subintervalo no qual uma raiz deve estar para processamento adicional.
def metodo_da_bissecao(equacao:symbols, intervalo:tuple , iteracoes_erro:tuple):

    if not teorema_bolzano(equacao, intervalo):
        return "Não existe zero no intervalo ou existe mais do que um zero pelo teorema de Bolzano"

    a , b = intervalo
    numero_de_iteracoes , tolerancia_de_erro = iteracoes_erro

    for i in range(numero_de_iteracoes-1): # -1 pq o range começa em 0.
        print(f"----------------------------------------------")
        print(f"-> Iteracao numero {i+1}:")
        c = a+((b-a)/2) # Ponto médio -> equivalente a (a+b)/2x
        print(f"\tPonto a: {a}\n\tPonto b: {b}\n\tPonto médio c: {c}")

        if equacao.subs('x',c) == 0 or (abs(b-a)/2) < tolerancia_de_erro :
            print(f"        Encontrámos raiz. <- SUCESSO")
            return c

        a, b = get_new_interval(a, b, c, equacao)
        print(f"        Nao encontrámos raiz. Definimos novo intervalo: [{a} , {b}]")
        print(f"----------------------------------------------")
        print(f"")
    return f"Atingimos o número máximo de {numero_de_iteracoes} iterações sem encontrar a raiz com a tolerância especificada."


