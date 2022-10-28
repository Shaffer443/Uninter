# Exercício 3

# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de Kwh consumida e o tipo de instalação: R para residência, I para industria e C para commércio.
# Caulcule o preço de acordo com a tabela:
# Residencial (r) - até 500 kwh = R$ 0,40 | acima == R$ 0,65
# Comercial (c) - até 100 kwh = R$ 0,55 | acima de 1000 == R$ 0,60
# Industrial (i) - até 5000 kwh = R$ 0,55 | acima 5000 == R$ 0,60

print('# Calcule seu Consumo de Energia Elétrica #')
print('Qual o tipo da sua instlação?')
print('- Residencial - R ')
print('- Comercial - C ')
print('- Industrial - I ')
print('\n')
tipo = input('qual o tipo de instalação: ')
consumo = float(input('Qual foi o seu consumo (Kwh): '))

if(tipo == 'R' or tipo=='r'):

        if(consumo <= 500):
            calculores = consumo * 0.40
            print('Seu consumo foi de {}. Totalizando um valor à pagar de R$ {}'.format(consumo, calculores))
        else:
            calculores = consumo * 0.65
            print('Seu consumo foi de {}. Totalizando um valor à pagar de R$ {}'.format(consumo, calculores))
elif(tipo == 'C' or tipo == 'c'):
    if(consumo <= 1000):
        calculocom = consumo * 0.55
        print('Seu consumo foi de {}. Totalizando um valor à pagar de R$ %.2f'.format(consumo, calculocom))
    else:
        calculocom = consumo * 0.60
        print('Seu consumo foi de {}. Totalizando um valor à pagar de R$ %.2f'.format(consumo, calculocom))
elif(tipo == 'I' or tipo == 'i'):
    if(consumo <= 5000):
        calculoind = consumo * 0.55
        print('Seu consumo foi de {}. Totalizando um valor à pagar de R$ %.2f'.format(consumo, calculoind))
    else:
        calculoind = consumo * 0.60
        print('Seu consumo foi de {}. Totalizando um valor à pagar de R$ %.2f'.format(consumo, calculoind))
else:
    print('Instalação Inválida')



