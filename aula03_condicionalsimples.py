# Condicional Simples

# Desenvolva um programa que lê dois valores numéricos inteiros e compara se o primeiro é meior que o segundo,
# utilizando uma condicional simples.

# Caso seja (resultado verdadeiro), ele imprime na tela a mensagem informando que o primeiro valor digitado é maior
# do que o segundo.

# obs: identação é importantíssimo. Pois, garante que a condição esteja dentro da condição.

# Exemplo 1:

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))

if(valor1 > valor2):
    print('O maior valor é o %i' %valor1)

print('O maior valor é o %i' %valor2)
