# Exercício 03

# Um Cinema cobra preços diferentes para os ingressos de acordo
# com a idade de uma pessoa.
# Se a pessoa tiver menos de 3 anos, o ingresso será gratuíto.
# Se tiver entre 3 e 12 anos, o ingresso custa R$ 15,00.
# Se tiver mais de 12 anos, custará R$ 30.

# 1 - Escreva um laço em que você pergunte a idade e informe o valor do ingresso.
# 2 - Encerre o laçõ usando break,q uando digitar 'sair'
# 3 - Após sair, informe o total de pessoas que compraram ingressos, e o total arrecado e a média da idade das pessoas.

print('\n')
print('# Cobrança de Preço - Cinema #\n')

pessoas = 0 # precisa estar antes do laço para contar e inicializar com zero
dinheiro = 0
somaidade = 0

while True:

        idade = input('Qual a sua idade? ')
        if (idade == 'fechar'):
            break

        idade = int(idade) # após a verificação da string, tranformando a idade em inteiro.
        pessoas += 1 # conta as pessoas, logo tem q estar após o break
        somaidade += idade # soma os valores da idade digitada
        if(idade < 3):
            ingresso = 0
            print('Menor de {} anos. Gratuidade no ingresso.'.format(idade))
        else:
            if(idade > 12):
                ingresso = 30
                print('Idade de {} anos. Valor do Ingresso é R$ 30,00.'.format(idade))
            else:
                ingresso = 15
                print('Idade de {} anos. Valor do ingresso é R$ 15,00.'.format(idade))
        dinheiro += ingresso # após o laço para contar os valores de referência
        mediaidade = somaidade / pessoas

print('\nTotal de {} Pessoa(s).'. format(pessoas))
print('Média da idade {0:.0f}.' .format(mediaidade)) # formata a saída da mediaidade
print('total arrecado de R$ {} .'. format(dinheiro))








