# Trabalhando Com Métodos Em Strings

# Uma String é Imútavel
# Mas, com listas podemos altera-las

#s1='algoritmos'
#print(s1)
#s1[0] = 'a'

# Dará erro, pois a string é imultável por si só

# Porém, em uma lista, ele pode ser alterada.
print('\n')
s2 = list('Algoritmos')
print(s2) # print separado
print(''.join(s2)) #print agrupado

# pelo fato dele separar por uma lista, podemos alterar a indexição [0], por exemplo
print('\n')
s2[0]='a'
print(''.join(s2))

# alguns métodos startswith (verifica um caracteres no início da string, retornando falso ou verdadeiro)
print('\n')
s3 = "lógica de programação e algoritmos"
boleano = s3.startswith('lógica')
print(boleano)

# alguns métodos endswith (verifica um caracteres no final da string, retornando falso ou verdadeiro)
print('\n')
s3 = "lógica de programação e algoritmos"
boleano2 = s3.endswith('algoritmos')
print(boleano2)

# lower e upper (converte a estrig para minusculo ou maiusculo)
print('\n')
s3 = "lógica de programação e algoritmos"
boleano3 = s3.upper().endswith('ALGORITMOS') # Se deixar sem o UPPER, daria falso, como passei tudo para maiúsculo, dará verdadeiro
print(boleano3)

# .count (conte a quantidade de vezes de uma determina string. sendo palavras, numeros frases )
print('\n')
s3 = "lógica de programação e algoritmos"
boleano4 = s3.count('a') # conta a quatidade de 'a' na string
print(boleano4)

# .split (divide uma string, sempre que encontrar espaços, tornando-as em uma lista)
print('\n')
s3 = "lógica de programação e algoritmos"
boleano5 = s3.split(' ') # ' ' colocara os itens divididos entre aspas simples, com um espaço dentro, como declarado
print(boleano5)

#Relação de métodos para validação de dados em string:
print('\n')
string = 'Lógica de Programação e Algoritmos'
numero = '42' # como string
numero1 = 42

# isanum - retorna verdadeiro para letras e numeros apenas
print(string.isalnum()) # retorna falso, pois tem espaços
print(numero.isalnum()) # retorna verdadeiro

# isalpha - somente letras e acentos
print('\n')
print(string.isalpha()) # retorna falso, pois tem espaços
print(numero.isalpha()) # retorna falso pois tem numeros
