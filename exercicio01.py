def exercicio_01():
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
        print(f'o numero digitado {numero} e PAR')
    else:
        print(f'o numero digitado {numero} e IMPAR')
#exercicio_01()
def exercicio_02():
    numero_01 = int(input('digite um numero: '))
    if numero_01 > 0:
        print('foi digitado um numero POSITIVO')
    elif numero_01 < 0:
        print('foi digitado um numero NEGATIVO')
    elif numero_01 == None:
        print('nao foi digitado numero')
#exercicio_02()
def exercicio_03():
    numero_02 = int(input('digite um numero: '))
    numero_03 = int(input('digite um numero: '))
    soma_numeros = numero_02 + numero_03
    if soma_numeros > 20:
        print(f'foi adicionado o numero 8 resultado: {soma_numeros + 8}')
    else:
        print(f'foi subitraido o numero 5 resultado: {soma_numeros - 5}')
#exercicio_03()
def exercicio_04():
    numero_04 = float(input('digite um numero: '))
    if numero_04 > 0:
        print(f'A raiz quadrade de {numero_04}:  {numero_04 ** 0.5:.2f}')
    else:
        print(f'o numero {numero_04} elevado ao quadrado {numero_04 ** 2}')
#exercicio_04()
#def exercicio_05():
