from Caixa.Biblioteca.visual import *


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
            dado[1] = float(dado[1])
            conta += dado[1]
        conta = str(conta).replace('.', ',')
        print(f'Fechamento do Dia: R${conta}')
    finally:
        a.close()
