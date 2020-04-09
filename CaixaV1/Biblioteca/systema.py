from datetime import date

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

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
        print(f'Arquivo {nome} Criado com sucesso')

    except:
        print('Houve um ERRO na criação do Arquivo')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        Cabeçalho('Pessoa Cadastrada','Azul')
        for linha in a:
            dado = linha.split(';') #quebra em elementos aquanto encontra o ;
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()

def cadastrarS(arq, prod, preco):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na leitura do arquivo')
    else:
        try:
            a.write(f'{prod};{preco}\n')
        except:
            print('Errou ao cadastrar os dados')
        else:
            print(f'{prod}, Foi adicionado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        contador = 1
        for linha in a:
            dado = linha.split(';') #quebra em elementos aquanto encontra o ;
            dado[1] = dado[1].replace('\n', '')
            dado[1] = dado[1].replace('.', ',')
            print(f'{contador} {dado[0]:<20} R$ {dado[1]:f>3} ')
            contador += 1
    finally:
        a.close()

def cadastrarP(arq, produto, preco):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na leitura do arquivo')
    else:
        try:
            a.write(f'{produto};{preco}\n')
        except:
            print('Errou ao cadastrar os dados')
        else:
            print(f'{produto}, Foi adicionado com sucesso')

def CalculoDia(nome):
    try:
        conta = 0
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in a:
            dado = linha.split(';') #quebra em elementos aquanto encontra o ;
            dado[1] = dado[1].replace('\n', '')
            dado[1] = dado[1].replace(',', '.')
            dado[1] = float(dado[1])
            conta += dado[1]
        conta = str(conta).replace('.', ',')
        print(f'Fechamento do Dia: R${conta}')
    finally:
        a.close()


hj = str(date.today())
if not arquivoExiste(hj):
    criarArquivo(hj)

if not arquivoExiste('Produtos'):
    criarArquivo('Produtos')

print(f'Data de Hoje {hj}')
while True:
    Cabeçalho('Copiadora Santo Antonio', 'Azul')
    Menu('Produtos Cadastrados', 'Cadastrar Produtos', 'Novo Pedido', 'Resumo do Dia', 'Saída')
    op = leiaInt('Digite a opção Desejada: ')

    if op == 1:
        Cabeçalho('Produtos Cadastrados', "Azul")
        lerArquivo('Produtos')
        input('')

    elif op == 2:
        Cabeçalho('Cadastrar novo Produto')
        produto = str(input('Novo Produto: '))
        preco = str(input('Preço do Produto: '))
        cadastrarP('Produtos', produto, preco)
        input('')

    elif op == 3:
        Cabeçalho('Novo Pedido')
        prod = str(input('Nome do Produto: '))
        preco = leiaMoeda('Informe o Preço: ')
        cadastrarS(hj, prod, preco)
        input('')

    elif op == 4:
        Cabeçalho('Resumo do Dia')
        lerArquivo(hj)
        CalculoDia(hj)
        input('')

    elif op == 5:
        Cabeçalho('Programa Encerrado', 'Vermelho')
        input('')
        break
    else:
        print('Favor Digitar um Numero entre 1 e 5')
        input('')
