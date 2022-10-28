# Exercício 02

# Escreva um algoritmo que leia dois calores numéricos e que pergunte ao usuário qual operação ele deseja realizar:
# adição, subtrção, multiplicação ou divisão. Exiba na tela o resulatdo da operação desejada.
print('\n')
print('CALCULADORA - AULA 3 | Exercício: 2')


valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um valor: '))

print('Qual operação deseja realizar?')
print('1 - Soma(Adição)(+)')
print('2 - Subtração(-)')
print('3 - Multiplicação(*)')
print('4 - Divisão(/)')

operacao = input('Qual operação deseja realizar? ')
# usei o input como string, pois ele caita tanto o simbolo (+, -, *, /), como o número inteiro como variável


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