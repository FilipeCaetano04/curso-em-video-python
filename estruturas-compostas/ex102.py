def fatorial(n = 1, show = False):
    """
    -> Calcula o faorial de um número.
    :parâmetro n: o número a ser calculada.
    :parâmetro show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """

    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show == True:
            if i > 1:
                print(f'{i} x ', end = '')    
            else:
                print(f'{i} = ', end = '')  
    return f  
    
    
fatorial(5, True)