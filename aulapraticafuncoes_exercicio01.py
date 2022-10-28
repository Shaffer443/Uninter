# Aula prática funções, exercício 01:

# Ecreva uma função que calcule o fatorial de um número recebido como parâmetro
# e retorne o seu resultado.
# Faça uma validação dos dados por meio de uma outra função, permitindo que somente valores positivos sejam aceitos.
# Crie o help da sua função.

def validacaointeiro(pergunta, min, max): # pode ser criada antes ou depois da função fatorial
    x = int(input(pergunta))              # forçar o usuário a inserir núemro interio e não muito alto. essa é a premissa.
    while((x < min) or ( x > max)): # validar o intervalo dentro do parâmetros que queremos.
        x = int(input(pergunta))
    return x # valor para vaidação e também servira para o input a ser fatorado
def fatorial(num): # vai fatorar um numero==(num)
    """
    Insira um número inteiro para que seja calculado sua fatoração.
    :param num: Digitar número inteiro (não aceita decimal)
    :return: Digitando zero (0), retornará o valor 1
             Digitando numerp inteiro, difernete de zero (0), se calcula a fatoração.
    """
    fatmin = 1 # valor da fatorial mínima
    if num==0:
        return fatmin # caso digite zero, retorne para 1 == fat
    for i in range (1, num+1, 1):   # lembrando que o for é até o valor limite -1.
        fatmin *= i                 #fat = fat *1 # i == operador.
    return fatmin                   # por isso somo +1, para ir até valor digitado para fatorar.
                                    # estou somadno um ao invés de diminuir um valor, por isso o +1(poderia ser -1 também)
                                    # o segundo retorno só funciona quando o numero for != de zero,
                                    # se não ele reponde ao primeiro return

# programa principal começa aqui
x = validacaointeiro('Digite um valor para calcular a fatoração: ', 1, 999) # delimintando o valor
                                                                             # do intervalo de validainteiro
print('{}! = {}'.format(x, fatorial(x)))                                     # chamando a função fatorial já no print.
                                                                             # primeiro X é o valor digitado no input

help(fatorial)

