# Strings e Listas dentro da lista
# Strings Dentro da Lista

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0]) # Indexação
print(mochila[0][0]) # Indexação Dupla
print(mochila[2][0]) # Indexação Dupla

# Varredura em indexação dupla
print('\n')

for item in mochila: # varre os itens (variável nomeado por mim), na variaével mochila.
    for letra in item: # dentro da mochila, procura uma letra ( variavel denominada por mim), dentro do item, dentro da mochila
        print(letra, end='') # mostra, as letras até o final (END) vazia.
    print() # mostra o que encontrou

# Varredura em indexação dupla por RANGE
print('\n')

for i in range(0, len(mochila),1): # declarei o tamanho len, já dentro da função. Pego o tamanho da lista.
    for j in range(0, len(mochila[i]),1): # pego o tamanho da string, dentro da lista.
        print(mochila[i][j], end='') # print com indece duplo
    print()

# Lista dentro de lista
print('\n')

mochila =[['Cebola', 0.39], ['Tomate', 0.49], ['Maça', 0.89]]

print(mochila[0][0])
print(mochila[2][1])

# Lista dentro de lista, solicitando os itens e informações ao usuário, com RANGE
print('\n')

item = [] # variável a ser povoada. Quarda os valores e dados difitados.
mercado = [] # variável com itens povoados. gera uma cópia dos itens em outra alocação da memoria

for i in range(3): # Lista máximad e 4 itens.
    item.append(input('Digite o nome do item: ')) # append - Acrescenta no item
    item.append(int(input('Digite a quantidade do item: ')))  # append - Acrescenta no item
    item.append(float(input('Digite o valor do item: ')))  # append - Acrescenta no item
    mercado.append(item[:]) # faz a cópia dos dados do ITEM em outra alocação de mémoria.
    item.clear() # Limpa a lista e segue para solicitar os dados do novo item. Sem isso, ele repetiria os dados já inclusos
print(mercado) # imprime| mostra os itens na vaiável mercado. os dados cópiados de iten, na memoria especifica.

# O Mercado = [] salva cada dado da variável item, fazendo uma cópia em outra alocação da variável Mercado[]

# print final da liista de compras:

soma = 0
print('Lista de compras:')
print('-'*20)
print('Item | Quantidade | Valor Unitário | Valor Total')
for item in mercado: # Varredura da lista intem em mercado
    print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    soma += item[1] * item[2]
print('-'*20)
print('Total a ser pago: R$ {}'.format(soma))

# Lista dentro de lista, solicitando os itens e informações ao usuário, modo masi simples.
print('\n')

mercado = [] # Variável odne alocará os dados da variável Item

for i in range(3):
    nome = input('Digite o nome do item: ')
    qtd = int(input('Digite a quantidade do item: '))
    valor = float(input('Digite o valor do item: '))
    mercado.append([nome, qtd, valor]) # salva os dados dos itens, nas variáveis nesta sequencia declarada no mercado
print(mercado)

# o povoamento aconteceu em variáveis simples nome, qtd e valor