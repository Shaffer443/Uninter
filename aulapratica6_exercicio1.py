# Exercício 1:

# Escreva um algoritmo que crie uma tupla com
# 10 palavras. Encontre dentro dessa tupla as
# vogais de cada palavra. Faça um print na tela
# com o nome da palavra e suas respectivas
# vogais

tuplas = ('casa','mar', 'sopa', 'predio','rua','cidade')

for tuplas in tuplas: # modo simplificado de FOR
    print('\nPalavra: {}, vogais: '.format(tuplas.upper()), end='') # deixa as palavras em maiúsculo
    for vogal in tuplas: # buca por volgais dentro das palavras
        if vogal.lower() in 'aeiou': # busca por uma determinação, no caso as vogais 'aeiou'.
            print(vogal.upper(), end=' ')        # end =' ' - não da quebra de linha e um espaço

# obs: sempre q tiver um método tem que haver um parêntese depois
# exemplo: vogal.lower (), vogal.upper()

