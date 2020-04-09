def Cor(msg, i='Branco'):
    cores = {'Branco':   f'\033[0;30m {msg} \033[m',
             'Vermelho': f'\033[0;31m {msg} \033[m',
             'Verde':    f'\033[0;32m {msg} \033[m',
             'Amarelo':  f'\033[0;33m {msg} \033[m',
             'Azul':     f'\033[0;34m {msg} \033[m',
             'Lilas':    f'\033[0;35m {msg} \033[m',
             'VerdeA':   f'\033[0;36m {msg} \033[m',
             'Cinza':    f'\033[0;37m {msg} \033[m'}
    return cores[i]

def Cabeçalho(msg, cor = "Branco"):
    print('-' * 32)
    print(Cor(msg.upper(), cor).center(42))
    print('-' * 32)

def Menu(*msg):
    contador = 1
    for c in msg:
        print(f'{contador} {c}')
        contador += 1
    print('-' *32)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(Cor(f'Erro por favor digite um número inteiro', 'Vermelho'))
            continue
        except(KeyboardInterrupt):
            print(Cor('Número Não Digitado','Vermelho'))
            return 0
        else:
            return n

def leiaMoeda(msg):
    n = input(msg)
    n = n.replace(',','.')
    try:
        n = float(n)

    except(ValueError, TypeError):
        print(Cor('Digite um preço valido', 'Vermelho'))
        return 0

    except(KeyboardInterrupt):
        print(Cor('Número Não Digitado', 'Vermelho'))
        return 0
    else:
        return n