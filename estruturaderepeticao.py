# Estrutura de Repetição

# Um dos modelos de repetição

x = 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)

# Estrutura de Repetição WHILE (ENQUANTO)
print('\n')

x = 1 # Variável declarada fora do loop
while (x<=5):
    print(x)
    x = x+1 # aqui informa que toda vez que se rodar uma vez o código, some 1 a X

# Exercício com Contador

print('\n')

# imprimir na tela somente valores dentro de um intervalo espeificado pelo usuário
# e que sejam números pares

inicial= int(input('Digite o valor para iniciar: '))
final=int(input('Digite o valor para finalizar: '))

x = inicial
while(x <= final):
    if(x % 2 == 0): # informa o resto zero, ou sej, que o número é par.
        print(x)
    x = x + 1 # prestar atenção o indetamento, pois ele que indico que está dentro ou não de um função
    # neste caso ele está dentro de WHILE, não de IF

# Exercício com Acumulador
print('\n')

# calcule a sua média de notas determinada disciplina
# Assumir que a média final é dada pela média artimética de cinco notas digitadas

soma=0
cont=1
while(cont<=5):
    nota = float(input('Digite a nota: ')) # linha do laço
    soma = soma + nota # linha do laço
    cont = cont + 1 # linha do laço
media = soma / 5 # linha fora do while
print(' Sua média das 5 notas é: %.2f' %media) # linha fora do while
