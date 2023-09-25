# Solução para Switch por meio de if, elif
# e else - ramificação branch
# ------------------------------------------
valor = 1
if valor == 1:
    print('O valor é {}'.format(valor))
elif valor == 2:
    print('O valor é {}'.format(valor))
else:
    print('O valor não foi encontrado.')
# ------------------------------------------
# Solução para Switch case por meio de
# dicinarios - pythonica pois Python trabalha
# com objetos de 1° ordem
# ------------------------------------------
valor = 1
valores = {
    1: 'O valor é 1',
    2: 'O valor é 2'
}
if valor in valores:
    print(valores[valor])
else:
    print('O valor não foi encontrado.')
# ------------------------------------------
# Solução para switch case por meio do
# pattern matching - PEP 634
# (feature de programação funcional)
# -> valor que quero dar match*
# ------------------------------------------
valor = 1
match valor:
    case 1:
        print('O valor é 1')
    case 2:
        print('O valor é 2')
    case _:
        print('O valor não foi encontrado.')
# ------------------------------------------
match list:
    case [1, 2, 3]:
        print('Lista')
    case [1, _, _]:
        print('O primeiro é 1')
    case [_, 2, _]:
        print('O segundo é 2')

match list:
    case [] | [_]:
        print('Um ou nenhum elemento')
    case [1, 2]:
        print('Lista = [1, 2]')
    case [1, *_]:  # Todo o restante não quero saber somente o 1°
        print('Um é o primeiro de uma lista > 1')
# ------------------------------------------
lista = [[]]  # Qualquer elemento seja inteiro, real, lista, tupla etc.
match lista:
    case [] | [_]:
        print('Vazio ou somente com um elemento')

# if isinstance(lista, list) and len(lista) == 0 or len(lista) == 1:
if isinstance(lista, list) and len(lista) in [0, 1]:
    print('Vazio ou somente com um elemento')
# ------------------------------------------
lista = [1, 2, 3, 4]
match lista:
    case [1, *resto]:
        print('O primeiro é 1 e o resto é {}'.format(resto))
        print(f'O primeiro é 1 e o {resto = }')
# ------------------------------------------
valor = 1
match valor:
    case 1 | 2:
        print('É igual a 1 ou 2')
# ------------------------------------------
lista = ['1', 2, 3]
match lista:
    case [] | [_]:
        print('Vazio ou somente com um elemento')
    case ['1', 2 | 2, _, _] | [_, 1 | 2, _]:
        print('Inicia com um ou dois')
    # O pipe | define o ou no switch case
    # Funciona com tipos diferentes
# ------------------------------------------
#   Dar nomes para usar depois
# ------------------------------------------
r = 1   # Pattern Matching tem o próprio escopo
cor = (255, 255, 255)   #somente rbg
cor = (255, 255, 255, 255)  #com alfa
match cor:
    case r, g, b:   # Tudo que tem vírgula no meio é considerado uma tuple em Python
        print(f'{r=}, {g=}, {b=}')
    case r, g, b, a:
        print(f'{r=}, {g=}, {b=}, {a=}')
    case r, g, b, a, h: # padrão cmic (len(5))
        print(f'{r=}, {g=}, {b=}, {a=}, {h=}')
# ------------------------------------------
#   Cláusula guardiã para grarantir
# ------------------------------------------
def chato_das_cores(cor):
    """

    :param cor:
    :return:
    """
    match cor:
        case r, g, b:
            return 'Cadê o alpha?'
        case r, g, b, a if a == 255:
            return 'Tudo transparente?'
        case r, g, b, a if r == 255:
            return 'Muito vermelho, não acha?'
        case r, g, b, a if g == 255:
            return 'Não!Muito verde!'
        case r, g, b, a if b == 255:
            return 'Azul? Sério?'
        case r, g, b, a:
            return 'Agora sim. :)'
help(chato_das_cores)
# ------------------------------------------
