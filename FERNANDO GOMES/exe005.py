numeros = []

while len(numeros) <= 2:
    numero = float(input(f'digite {len(numeros)+1}° um numero: '))
    numeros.append(numero)
    
print()
print('os numeros digitados foram ')
for a,c in enumerate(numeros):        
    print(f'{a+1}° >> {c}')
    
print()
    