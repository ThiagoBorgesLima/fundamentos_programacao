# Códigos retirados da Documentação Oficial
# Calcula os valores da Sequencia de Fibonacci

# Escreve na tela a série de Fibonacci até o elemento n
def fib(n):    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# Devolve a série de Fibonacci até o elemento n
def fib2(n):   
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result