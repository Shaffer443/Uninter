# Aula pratica 04
# Exercício 01

# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário
# qual operação ele deseja realizar: Adição, Subtração, Multiplicação, Divisão e sair.
# Exiba na tela o resultado
# Repita até que a opção saída seja escolhida.

print('CALCULADORA - AULA 3 | Exercício: 2')




print('Qual operação deseja realizar?')
print('1 - Soma(Adição)(+)')
print('2 - Subtração(-)')
print('3 - Multiplicação(*)')
print('4 - Divisão(/)')

operacao = input('Qual operação deseja realizar? ')
# usei o input como string, pois ele caita tanto o simbolo (+, -, *, /), como o número inteiro como variável

valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um valor: '))


while(operacao != 's' ):
    if(operacao == 1 or operacao == '+'):
        soma = valor1 + valor2
        print('O resultado da soma {} + {} é = {}'.format(valor1, valor2, soma))
    elif(operacao == 2 or operacao == '-'):
        subtracao = valor1 - valor2
        print('O resultado da subtração {} + {} é = {}'.format(valor1, valor2, subtracao))
    elif(operacao == 3 or operacao == '*'):
        multiplicacao = valor1 * valor2
        print('O resultado da mutiplicação {} + {} é = {}'.format(valor1, valor2, multiplicacao))
    elif(operacao == 4 or operacao == '/'):
        divisao = valor1 / valor2
        print('O resultado da divisão {} + {} é = {}'.format(valor1, valor2, divisao))
    else:
        print('Numero digitado não corresponde a nenhuma operação.')

    print('Qual operação deseja realizar?')
    print('1 - Soma(Adição)(+)')
    print('2 - Subtração(-)')
    print('3 - Multiplicação(*)')
    print('4 - Divisão(/)')

    operacao = input('Qual operação deseja realizar? ')

    if(operacao != 's'):
        valor1 = float(input('Digite um valor: '))
        valor2 = float(input('Digite um valor: '))
    # usado para que ele não leia mais os valores após o 's'


print('Fechando Programa...')