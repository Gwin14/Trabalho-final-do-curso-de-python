import funcoes
import alternativas

resposta = input(alternativas.res)

if resposta == '1':
    funcoes.sobrevientesMortos()
elif resposta == '2':
    funcoes.porcentagemMortosMaiorDeIdade()
elif resposta == '3':
    funcoes.mortosPorClasse()
elif resposta == '4':
    funcoes.quantidadeDeConjulgues()
elif resposta == '5':
    funcoes.locaisDeEmbarque()
else:
    print('Insira uma resposta válida.')
