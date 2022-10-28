# Docstring

def soma(x=0, y=0, z=0): # com parâmetro opcional. ou seja, aceita zero ou não colocar valor
    """
    Função que soma até três valores inteiros.
    :param x: Valor inteiro (opcional)
    :param y: Valor inteiro (opcional)
    :param z: Valor inteiro (opcional)
    :return: soma inteira dos valores declarados
    """
    return x+y+z


print(soma(3,2)) #equivalente a x=3, y=2 e z=0
help(soma) # se não escrever nada, ele retornará o cabeçalho da função.
            # ajuda da função