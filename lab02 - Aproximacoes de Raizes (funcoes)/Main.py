from os.path import split

from Metodo_Bissecao import *
from Metodo_Newton import *
from Metodo_Secante import *

# π = '960' valor do caracter
# ℯ = '8495' valor do caracter
def equacao_para_simPy(equacao: str):
    equacao = equacao.replace('^', '**')
    equacao = equacao.replace('sen', 'sin')
    equacao = equacao.replace('tg', 'tan')
    equacao = equacao.replace('e', 'exp(1)')
    equacao = equacao.replace('ℯ', 'exp(1)')
    equacao = equacao.replace('π', 'pi')

    return sympify(equacao)

def equacao_para_string(equacao:str ):
    equacao = str(equacao)
    equacao = equacao.replace('**', '^')
    equacao =equacao.replace('exp(1)', 'e')
    equacao = equacao.replace('*', '*')
    equacao = equacao.replace('pi', 'π')
    return equacao

def intervalo_para_tuple(intervalo:str):
    if ' ' in intervalo :
        intervalo = intervalo.split(' ')
    elif ',' in intervalo:
        intervalo = intervalo.split(',')
    if intervalo[0] == 'pi' :
        a = float(pi)
        b =intervalo[1]
    elif intervalo[1] == 'pi':
        a = intervalo[0]
        b = float(pi)
    elif intervalo[0] == 'e':
        a = float(exp(1))
        b = intervalo[1]
    elif intervalo[1] == 'e':
        a = intervalo[0]
        b = float(exp(1))
    else:
        a = float(intervalo[0])
        b = float(intervalo[1])

    return a , b

def main():

    try:
        while true:

            print("--------------------------------------------------------------")
            equacion = str(input("Qual é a equação que pretende encontrar o zero? Ex: x^2+x-6\n"))
            equacion = equacao_para_simPy(equacion)
            intervalo = str(input("Em que intervalo? Ex: -5,5 [Sem parentesis] \n"))
            intervalo = intervalo_para_tuple(intervalo)
            print('1) Metodo da Bisseção \n2) Metodo de Newton \n3) Metodo da Secante')
            metodo = int(input("Qual o método que deseja aplicar? \n"))

            if metodo == 1:
                resposta = metodo_da_bissecao(equacion, intervalo, ITERACOES_E_ERROS_BISSECAO)
                print(f"A equação--> " + equacao_para_string(equacion) + " é o ponto x = " + str(resposta))
            elif metodo == 2:
                resposta = metodo_de_newton(equacion, intervalo, ITERACOES_E_ERROS_NEWTON)
                print(f"A equação--> " + equacao_para_string(equacion) + " é o ponto x = " + str(resposta))
            elif metodo == 3:
                resposta = metodo_da_secante(equacion, intervalo, ITERACOES_E_ERROS_SECANTE)
                print(f"A equação--> " + equacao_para_string(equacion) + " é o ponto x = " + str(resposta))
            print("--------------------------------------------------------------")

    except ValueError as e:
        print(f"Erro: {e}")



if __name__ == "__main__": #se o ficheiro for corrido diretamente, chama a funçao main. se for importado como modulo, nao corre a funçao a nao ser que seja chamada
    main()