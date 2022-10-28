# Escopo de variáveis

# Global - pode ser invocada ao longo do programa. Desde que esteja criada no programa principal

# função Global:

print('Exemplo 1 - Global')

def comida():
    print(ovos)
# Programa Principal
ovos = 12 # variável criada dentro do esocpo global
comida()

# Estou usando o programa principal, odne o mesmo irá condicionar a variável OVOS
# declarada para resultar na mesma, que está sendo chamda na função principal - print(ovos)

print('Exemplo 1 - Local')

# função Local:

def comida2():
    ovos = 10 # por estar localmente não interfere no ovos global.
    bacon() # por estar chamando uma função local, não oferece resultado dentro da função comida2
    print(ovos) # print de ovos 10, e não 6 do bacon. por ser o print da variável deste escopo local

def bacon():
    ovos = 6 # por estar localmente não interfere no ovos global, nem local

# Programa Principal

comida2()

# Irá aparecer ovos 10, devido a OVOS ter sido declarada localmente na função comida2

# funções Locais e Globais

print('Exemplo 1 - Local e Global:')

def comida3():
    ovos = 'Variável Local de Comida 3'
    print(ovos) # printa a variável ovos de comida 3

def bacon2():
    ovos ='Variável local de Bacon 2'
    print(ovos) # printa variável ovos dentro de bacon 2
    comida3()
    print(ovos) # printa a variável ovos de bacon2() novamente.

# Programa Principal

# Variáveis de mesmo nome globalmente e localmente, a local tem soberania sobre a local.
# logo, assume no lugar da global.

ovos = 'Variável Global'
bacon2() # printa a variável ovos de bacon 2, depois a de comida 3, dentro de de comida3(), depois a de bacon 2().
print(ovos) # printa a variável global ovos

# instrução Local
print('Exemplo 1 - Instrução Global:')

def comida4():
    global ovos # quando se deckara que o valor de ovos é global, ele altera o valor de ovos local para ser impresso no global
    ovos = 'Comida 4'

# programa principal

ovos = 'Global'
comida4()
print(ovos) # imprimirá o valor de ovos local, ou seja, 'comida 4'
