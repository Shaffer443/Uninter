# Recursos Avançados de Laços em Python

# calcule a sua média de notas determinada disciplina
# Assumir que a média final é dada pela média artimética de cinco notas digitadas

soma=0
cont=1
while(cont<=5):
    nota = float(input('Digite a nota: ')) # linha do laço
    soma += nota # linha do laço # soma = soma + nota (significa)
    cont += 1 # linha do laço # cont = cont + 1 (Significa)
media = soma / 5 # linha fora do while
print(' Sua média das 5 notas é: %.2f' %media) # linha fora do while