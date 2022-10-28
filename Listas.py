# Listas

# Indexadas por valores numericos inteiros
# Estrutura de dados dinâmica
# representada por colchetes []

# Indices:    0          1         2         3
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
# Indices:    0          1         2         3
mochila1 = ['Machado', 'Camisa', 'Bacon', 'Abacate']

# perceba a formatção que o puthon já fornece ()
print('Tuplas: ', mochila)
# perceba a formatção que o puthon já fornece []
print('Listas: ', mochila1)

# como a lista é mutável, pode-se aluterar um dado.
print('\n')
mochila1[3] = 'Laranja'
print('Lista: ', mochila1)
# Retornará com laranja no lugar do abacate

# Adicionando indice | Elemento na Lista:
print('\n')
mochila1.append('Ovos')
print('Lista: ', mochila1)
# Iten fica adicionado no final da "matriz" | Lista, desta forma

# inserir um iten|objeto em uma posição expecífica:

print('\n')
mochila1.insert(0,'Canivete') # 1 - local a ser inserido na matriz da lista, e objeto| dado a ser inserido.
                                # 0 = Primeiro da matriz, 1 =  segundo da matriz, etc.
print('Lista: ', mochila1)


# Remover um iten|objeto em uma posição e expecíficamente:
print('\n')

del mochila1[0] # remove o item da variável mochila na posição da matriz [0], usando a função del

mochila1.remove('Ovos') # remove um item expecifico, no caso, nominlamente. a função acha-o dentro da variável e exclui

print('Lista: ', mochila1)


# Váriável de Referencia;
print('\n')
# No python, se vc alterar um variável, fazendo um cópia, ele também alterará a variável de origem

x = [5,7, 9,11]
y = x # referencia/cópia de X, aponta para a mesma memória alocada
print(x)
print(y)
# perceba que são identicas, pois Y é uma cópia de X, com o apontamento para a mesma memória alocada.
# logo, se alterar Y, também alterará X
print('\n')
y[0]=2
print(x)
print(y)

# Para que isto não ocorrar, precisa fazer uma cópia em uma memória, qeu seja apontada diferente da original
print('\n')
x1=[5,7,9,11]
y1=x1[:] # referencia/cópia de X, aponta para memórias diferentes de alocação
print(x1)
print(y1)

# diferença do [:] que informa para ser cópiada X em outro local de memória. por isso mostrará difente alterando-o
print('\n')
y1[0]=2
print(x1)
print(y1)
