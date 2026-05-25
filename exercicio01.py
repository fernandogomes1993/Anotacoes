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
def exercicio_05():
    numero_02 = int(input('digite um numero: '))       
    if numero_02 % 5 == 0:
        print('o numero informado e divisiveis por 5')
    else:
        print('o numero informado não e divisivel por 5')
#exercicio_05()
def exercicio_06():
    numero_02 = int(input('digite um numero: '))
    numero_03 = int(input('digite um numero: '))
    
    if numero_02 % numero_03 == 0:
        print('o numero e divisivel ')
    else:
        print('o numero não e divisivel')
def exercicio_07():
    valores = []
    
    while len(valores) < 3:
        valor = int(input(f'informe {len(valores)+1}º numero inteiro: '))
        if valor not in valores:
            valores.append(valor)
        else:
            print()
            print('numero invalido informe outro')
            print()
    valores = sorted(valores)
    A = valores[0]
    B = valores[2]
    C = valores[1]
    print()
        
    print('Menor: ',A)      
    print('Maior: ',B) 
    print('Inter: ',C)      
def exercicio_08():
    numero_inteiro = int(input('informe um numero inteiro: '))
    if numero_inteiro >= 20 and numero_inteiro <= 90:
        print(f'o numero {numero_inteiro} esta entre 20 e 90')
    else:
        print('o numero não esta na faixa de valores')
def exercicio_09():
    valor_venda = float(input('forme o valor de venda: '))  
    if valor_venda < 10:
        print(f'valor da venda: R$ {valor_venda + (valor_venda * 0.07)}')
    elif valor_venda < 30:
        print(f'valor da venda: R$ {valor_venda + (valor_venda * 0.05)}')
    elif valor_venda < 50:
        print(f'valor da venda: R$ {valor_venda + (valor_venda * 0.04)}')
    elif valor_venda >= 50:
        print(f'valor da venda: R$ {valor_venda + (valor_venda * 0.03)}')

