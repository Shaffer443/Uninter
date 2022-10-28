# For x While

# for - usado para numeros finitos
# while - numero infinitos

# for:

for i in range (1,6,1):
    print(i)
# i = variável de controle (nome usado)
# 1,6,1 = valor inicial do iterador, valor final do iterador, contador|passo do iterador

# while
print('\n')

x = 1
while(x<6):
    print(x)
    x=x+1

# Valor inicial do iterador x = 1, ou seja, 1
# valor final do iterador, dentro do while - x<6
# contador|passo do iterado - x = x + 1

# a) Inteiro de 3 até 12, com 12 incluso.
print('\n')

# for:

for a1 in range(3,13,1):
    print(a1)

# while:
print('\n')

a2 = 3
while(a2 <= 12):
    print(a2)
    a2 += 1

# b) Inteiros de 0 até 9, excluindo 9, com passo de 2

# for:
print('\n')

for b1 in range(0,9,2):
    print(b1)

# while:
print('\n')

b2 = 0
while(b2<9):
    print(b2)
    b2+=2