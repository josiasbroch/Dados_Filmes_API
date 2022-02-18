import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('https://www.omdbapi.com/?t='+titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro de conexao')
        return None

def detalhes_do_filme(filme):
    print('Titulo:', filme['Tilte'])
    print('Atores:', filme['Actors'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Nota:', filme['imdbRating'])
    print('-' * 20)

sair = False
while not sair:
    op = input('Digite o filme desejado ou SAIR para fechar:')

    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == "False":
            print('Filme nao encontrado')
        else:
            detalhes_do_filme(filme)