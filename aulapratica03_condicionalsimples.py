# Condicional Simples

# Traduza as afirmações a seguir para condicionais em Python

# a) Se a idade é maior que 60, escreva: "Você tem direitos aos benefícios"
# b) Se dano é maior do que 10 e escudo é igual a 0, escreva: "Você está Morto!"
# c) Se pelo menos uma das variáveis booleanas norte,sul, leste e oeste resulatrem em True, escreva: "Você Escapou!"

# a)

idade = int(input('Digite sua idade: '))
if(idade > 60):
    print('Você tem direitos aos benefícios')

# b)

b = int(input('Digite o valro do seu dano(Ataque): '))
b1 = int(input('Digite o valor do Escudo (Defesa): '))
if(b>10 and b1 == 0):
    print('Você esta morto!')

# c)
# A questão não pediu, mas temos que criar as variáveis
if(norte==True or sul==True or leste==True or oeste==True):
    print('Você Escapou!')
