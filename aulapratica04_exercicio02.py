# Escreve um algoritmo que leia um valor e que imprima a quantidade de cédulas
# necessárias ara pagar esse mesmo valor.
# Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de:
# R$ 100, 50, 20, 10, 5 e 1.

print('\n')
print('### Simulação de um Caixa Eletrônico Simples ###\n')


valor = int(input('Digite o valor (R$)? '))

# precisa ser usado ifs simples, pois não é uma condição de verdadeiros e falsos

while True:
    # 100
    if valor >=100:
        cedulasd100 = valor // 100
        valor -= cedulasd100 * 100
        print('{} cedula(s) 100'.format(cedulasd100))
        if not valor:
            break
    # 50
    if valor >=50:
        cedulasd50 = valor // 50
        valor -= cedulasd50 * 50
        print('{} cedula(s) 50'.format(cedulasd50))
        if not valor:
            break
    # 20
    if valor >=20:
        cedulasd20 = valor // 20
        valor -= cedulasd20 * 20
        print('{} cedula(s) 20'.format(cedulasd20))
        if not valor:
            break
    # 10
    if valor >=10:
        cedulasd10 = valor // 10
        valor -= cedulasd10 * 10
        print('{} cedula(s) 10'.format(cedulasd10))
        if not valor:
            break
    # 5
    if valor >=5:
        cedulasd5 = valor // 5
        valor -= cedulasd5 * 5
        print('{} cedula(s) 5'.format(cedulasd5))
        if not valor:
            break
    # 1
    if valor: # pega o valor que sobra <=4 e contabiliza. não precisa de calculo
        cedulasd1 = valor
        print('{} cedula(s) 1'.format(cedulasd1))
        break

# o IF NOT VALOR - Significa que se não houver mais valor a se analisado ele para o código