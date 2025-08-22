"""
Trabalho AN - 1
Programa em PYTHON que realiza a mudança de base de um número real qualquer (por exemplo 853674,07523901 ou -853674,07523901) entre duas bases quaisquer entre 2 e 62.
Para os algarismos entre 10 e 35, deverá usar letras maiúsculas A, B, C, ...
Para os algarismos entre 36 e 61 usar letras minúsculas a, b, c, ....
Dadas uma base atual e uma nova base (entre 2 e 62), o programa deverá de ser capaz de escrever qualquer número real (dado na base atual) na nova base.
Para cálculos não exatos, podemos dar o problema por terminado quando se fixarem 8 casas decimais.
"""

# Constante para o limite de casas decimais
DECIMAL_LIMIT = 8

# Funções de Mapeamento de Dígitos - Alternativa ao Array ALPHABET.
# É preferivel isto ao array ALPHABET, pois nao tenho de estar constantemente a aceder a um array, o que reduz a complexidade do algoritmo
# assim como reduz o numero de linhas de codigo necessarias para fazer a passagem. (nao preciso de fazer um FOR)
def valor_para_char(valor):
    if 0 <= valor <= 9:
        return str(valor)
    elif 10 <= valor <= 35:
        return chr(valor + 55)  # "A" = 65, então 65 - 10 = 55
    elif 36 <= valor <= 61:
        return chr(valor + 61)  # "a" = 97, então 97 - 36 = 61
    else:
        raise ValueError("Valor inválido para conversão em caractere.")

# Mesmo caso da funcao anterior, mas ao contrario.
def char_para_valor(char):
    if char.isdigit():
        return int(char)
    elif 'A' <= char <= 'Z':
        return ord(char) - 65 + 10 #ord retorna o valor ASCII do char
    elif 'a' <= char <= 'z':
        return ord(char) - 97 + 36
    else:
        raise ValueError(f"Caractere inválido para conversão em valor: {char}")

############################################################### Funções de Validação ########################

def validar_base(base):
    if not 2 <= base <= 62:
        raise ValueError("Base inválida. Deve ser entre 2 e 62.")


def validar_numero(numero, base):
    caracteres_validos = []
    for i in range(base): #range(base) serve apenas para o ciclo iterar o numero correto de vezes
        caracteres_validos.append(valor_para_char(i))

    caracteres_validos.append('.') #adiciona o ponto à lista de caracteres validos
    for char in numero:
        if char not in caracteres_validos and char != '-':
            raise ValueError(f"Caractere inválido '{char}' para a base {base}.")


def validar_bases(numero, base_atual, base_nova):
    validar_base(base_atual)
    validar_base(base_nova)
    validar_numero(numero, base_atual)

################################################# Funções de Separação do Número ############################


def get_sinal(numero):
    if numero.startswith('-'):
        return -1, numero[1:]
    return 1, numero


def get_parte_inteira(numero):
    if '.' in numero:
        return numero.split('.')[0]
    return numero


def get_parte_decimal(numero):
    if '.' in numero:
        return numero.split('.')[1]
    return ''

########################################################## Funções de Conversão base 10 ####################


# Esta funcao nao tem de verificar se nada é valido, porque isso é feito no começo, quando o input é dado.
# Esta funcao apenas tem de converter o numero para base 10, pelo que o return vai sempre ser um numero, nao deverá ser string.
# Na tua versão tens "i" por exemplo que para nós nao diz nada quando estamos a ler o codigo, por isso é preferivel usar nomes mais descritivos.
"""
Esta função é responsável por converter um número de qualquer base para a base 10.
O metodo é similar ao procedimento em papel, visto em aula.

A conversao para base 10 é simplesmente multiplicar cada digito pelo valor da base elevado à sua posição.
Por exemplo, para o numero 123 na base 5, o 1 é multiplicado por 5^2, o 2 por 5^1 e o 3 por 5^0.
"""
def converter_para_base_10(numero, base):
    valor_total = 0.0
    expoente = 0
    if '.' in numero:
        parte_inteira, parte_decimal = numero.split('.')
    else:
        parte_inteira = numero
        parte_decimal = ''

    # Converter parte inteira
    for digito in reversed(parte_inteira): #reversed para que o digito mais à direita seja o de indice 0 (para bater certo com o expoente = 0 acima)
        valor = char_para_valor(digito) #converte o digito para um valor
        valor_total += valor * (base ** expoente)
        expoente += 1

    # Converter parte decimal
    expoente = -1
    for digito in parte_decimal: #sem reversed, e o expoente começa em -1 e vai decrementando
        valor = char_para_valor(digito) #converte o digito para um valor
        valor_total += valor * (base ** expoente)
        expoente -= 1

    #o valor_total vai sempre sendo atualizado, pelo que chegando aqui é só retornar o valor
    return valor_total

"""
Esta função é responsável por converter a parte inteira de um número de base 10 para uma nova base.
O metodo é similar ao procedimento em papel, visto em aula.

Em papel, terminamos quando o numero que sofrerá mais uma divisao é 0 (na sua parte inteira), o que significa que é o ultimo passo.
"""
def converter_de_base_10_parte_inteira(numero, base):

    if numero == 0:
        return '0'
    digitos = []
    while True:
        resto = numero % base
        digitos.append(valor_para_char(int(resto)))
        numero = numero // base
        if numero < base:  # criterio de paragem é o numero resultante da divisao ser menor que a base. se for menor é porque ja nao é possivel dividir pelo numero.
            digitos.append(valor_para_char(int(numero)))
            break
    return ''.join(reversed(digitos))

"""
Esta função é responsável por converter a parte decimal de um número de base 10 para uma nova base.
O metodo é similar ao procedimento em papel, visto em aula.

O "input" desta funçao é um numero decimal com parte inteira 0 e parte decimal diferente de 0.
o numero começa pelo numero dado e é multiplicado pela base nova, o que resulta num numero inteiro com parte decimal.
A parte inteira desse numero é convertida para a base nova e adicionada à lista de digitos.
O proximo numero a multplicar pela base é a parte decimal do numero resultante da multiplicação anterior.
"""
def converter_de_base_10_parte_decimal(numero, base):
    digitos = []
    contador = 0
    while numero > 0 and contador < DECIMAL_LIMIT: # criterio de paragem é a parte decimal de "numero" ser 0 ou o contador chegar a 8 (limite imposto pelo enunciado)
        numero *= base
        parte_inteira = int(numero)
        digitos.append(valor_para_char(parte_inteira))
        numero -= parte_inteira
        numero = round(numero, DECIMAL_LIMIT) ##AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        contador += 1
    return ''.join(digitos)

##################################################################### PRINCIPAIS ###########################

# Função para juntar as partes inteira e decimal
def juntar_partes(parte_inteira, parte_decimal):
    if parte_decimal:
        return f"{parte_inteira}.{parte_decimal}" #o f antes de " é para indicar que é uma string formatada( e tem o ponto entre as partes)
    return parte_inteira


# Função Principal de Mudança de Base
"""
Esta função é responsável por "juntar" todos os metodos acima descritos, com fim a converter um numero de uma base para outra.
Esta abordagem foi a escolhida tendo em conta a facilidade de leitura do código, e a separaçao de funçoes
"""
def mudar_base(numero, base_atual, base_nova):
    validar_bases(numero, base_atual, base_nova)

    sinal, numero = get_sinal(numero)
    parte_inteira_str = get_parte_inteira(numero)
    parte_decimal_str = get_parte_decimal(numero)

    # Se a base atual for igual à base nova, retornar o número original
    if base_atual == base_nova:
        return ('-' if sinal == -1 else '') + numero

    # Converter para base 10
    numero_em_base_10 = converter_para_base_10(numero, base_atual)
    parte_inteira_base10 = int(numero_em_base_10)
    parte_decimal_base10 = numero_em_base_10 - parte_inteira_base10

    # Converter da base 10 para a base nova
    parte_inteira_nova_base = converter_de_base_10_parte_inteira(parte_inteira_base10, base_nova)
    parte_decimal_nova_base = converter_de_base_10_parte_decimal(parte_decimal_base10, base_nova)

    numero_nova_base = juntar_partes(parte_inteira_nova_base, parte_decimal_nova_base)

    return ('-' if sinal == -1 else '') + numero_nova_base


#Funcao de testes - a ser comentada antes de submissão

def testes():
    print("Base inferior a 10 para 10")
    print("01010101 (2) -> 85 (10): resposta do programa ->", mudar_base("01010101", 2, 10))
    print("0111101 (2) -> 61 (10): resposta do programa ->", mudar_base("0111101", 2, 10))
    print("--------------")
    print("Base superior a 10 para 10")
    print("CC12A (30) -> 10044970 (10): resposta do programa ->", mudar_base("CC12A", 30, 10))
    print("CC12A.123 (30) -> 10044970.03566666 (10): resposta do programa ->", mudar_base("CC12A.123", 30, 10))
    print("--------------")
    print("Base 10 para inferior a 10")
    print("123 (10) -> 1111011 (2): resposta do programa ->", mudar_base("123", 10, 2))
    print("123.25 (10) -> 1111011.01 (2): resposta do programa ->", mudar_base("123.25", 10, 2))
    print("--------------")
    print("Base 10 para superior a 10")
    print("123 (10) -> 7B (16): resposta do programa ->", mudar_base("123", 10, 16))
    print("123.456 (10) -> 7B.74 (16): resposta do programa ->", mudar_base("123.456", 10, 16))

########################### MAIN ###############################################################################
"""
Esta função é responsável por pedir o input, chamar a funçao que faz a mudança de base e imprimir o resultado.
"""
def main():

    #testes() #comentar antes de submissão
    try:
        numero = input("Insira o número: ")
        base_atual = int(input("Insira a base atual (2-62): "))
        base_nova = int(input("Insira a base nova (2-62): "))

        resultado = mudar_base(numero, base_atual, base_nova)
        print(f"O número {numero} na base {base_atual} é igual a {resultado} na base {base_nova}.")

        resultado_inverso = mudar_base(resultado, base_nova, base_atual)
        print(f"Verificação: O número {resultado} na base {base_nova} é igual a {resultado_inverso} na base {base_atual}.")
    except ValueError as e:
        print(f"Erro: {e}")


#isto aqui pra baixo nao é absolutamente necessario mas nnc se sabe qd vamos querer usar isto noutro projeto e entao já salvaguarda o caso de ser importado por outro .py
if __name__ == "__main__": #se o ficheiro for corrido diretamente, chama a funçao main. se for importado como modulo, nao corre a funçao a nao ser que seja chamada
    main()
##############################################################################################################
