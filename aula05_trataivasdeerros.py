# Recursos avançador com Funções - Erros

# exemplo 1:
print("Exemplo 1")

while True: # T maiusculo
  try: # tentar rodar
    x = int(input('Digite um número: '))
    break
  except ValueError: # caso haja este erro
      print('Erro de digitação, Revise o valor digitado.')


# Exemplo 2:
print('\n')
print("Exemplo 2")
def div(): # função criada
    try: # o que a função vai tentar fazer
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1/num2
    except ZeroDivisionError: # se este erro ocorrer
        print('Erro. Não pode se dividir por zero(0)')
    except:
        print('Erro. Verifique os valores') # Qualquer outro erro não declarado
    else:
        return res # retorna o valor de algo. no caso o resultado == res. Se tudo ocorrer corretamente
    finally: # É sempre executado após o try. Signifca o final. Cai aqui de qualquer jeito
        print('Executará sempre!')

# Programa Principal

print(div()) # mostrar o programa div()

# Exemplo 3:
# Função como parâmetro de Função.
print('\n')
print("Exemplo 3")

def imprime_com_condicao(num, fcond):
    if fcond(num):
        print(num)

def par(x):
    return x%2==0
def impar(x):
    return not par(x)

# programa principal

imprime_com_condicao(5, impar) # verifica se o num(5) é impar, se for imprime.
                            # Se trocar o impar para par, ou mudar o número fará as verificações

# Exemplo 4:
# Função lambda.
# função em uma só linha
print('\n')
print("Exemplo 4")

res = lambda x:x*x
print(res(3)) # declara o valor de X, para ser elevado ao quadrado (calculo de x*x)
            # valores declarados direto no print
soma = lambda x,y: x+y
print(soma(3,5)) # declara os valores de X e Y. direto no print