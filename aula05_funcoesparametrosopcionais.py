# Funções Parâmetros opcionais

# quando podemos não usar todos os parâmetros de uma função. Ser seletivo.

def soma (x, y, z):
    res=x+y+z
    print(res)

# logo:

soma(2,3,4) # somando todas variáveis
soma(x=0,y = 3,z = 4) # o X foi omitido e somando as demais variáveis
soma(x=0, y=0, z = 4) # o X e Y foi omitido e somando as demais variáveis
soma(x=0, y=0, z=0) #Todas as variáveis foram omitidas

# outro modo:

print('\n')
# chamasse cabeçalho da função
def soma2(x=0, y=0, z=0):
    res= x+y+z
    print(res)

# resultados chamando a função
# pegando a ordem sempre x -> y -> z

soma2(1,2,3)
soma2(1,2) #z omitido
soma2(1) # y e z omitido
soma2() # todos omitidos
