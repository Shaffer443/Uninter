# Concatenação#

a = 'minha Casa '
a = a + 'é azul'
print(a)

b = 'R'+'-'*3+'a'+'-'*2+'f'+'-'*4+'a'+'-'*5 #multiplicando os hifens e somando as letras#
print(b)

# composição #

nota = 8.5
c = 'sua nota é %f' % nota
d = 'sua nota é %.1f' % nota # limitador de casas decimais #
print(c)
print(d)

# Mais de uma variável #

disciplina = 'python'
e = 'sua nota é %.1f em %s' % (nota, disciplina)
print(e)

# reescrevendo #
f = 'Sua nota é {} em {}'.format(nota, disciplina) # pattern mais usual #
print(f)

# fatiando string #

g = 'Rafael José Gouveia de Melo'
print(g[0:11]) # Como em um excel, estou selecionando o caractere que quero imprimir, delimitando até o 11, dentre um determinado espaço, no caso de 0 a 11#
print(g[:6]) # Outro modo é não declarar nada no começo e ele vai do inicio até onde foi delmitado #

# tamanho, quantidade de caracteres em uma string (lenght) #

tamanho = len(g)
print(tamanho) # Qauntidade de carcteres na string g#