import funcoes
import alternativas

resposta = input(alternativas.res)

if resposta == '1':
    funcoes.sobrevientesMortos()
elif resposta == '2':
    funcoes.porcentagemMortosMaiorDeIdade()
elif resposta == '3':
    funcoes.mortosPorClasse()
else:
    print('Insira uma resposta válida.')
        