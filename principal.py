import tkinter as tk
import funcoes


def executar_acao(opcao):
    if opcao == 1:
        funcoes.sobrevientesMortos()
    elif opcao == 2:
        funcoes.porcentagemMortosMaiorDeIdade()
    elif opcao == 3:
        funcoes.mortosPorClasse()
    elif opcao == 4:
        funcoes.quantidadeDeConjulgues()
    elif opcao == 5:
        funcoes.locaisDeEmbarque()
    elif opcao == 6:
        funcoes.tarifasPagas()
    elif opcao == 7:
        funcoes.relacaoIdadeSobreviventes()
    elif opcao == 8:
        funcoes.totalDeParentes()
    elif opcao == 9:
        funcoes.sobreviventesPorGenero()
    elif opcao == 10:
        funcoes.mediaPrecosPorClasse()


def criar_janela():
    janela = tk.Tk()
    janela.title('Menu de Opções')

    estilo_botao = {'font': ('Arial', 12), 'height': 2, 'width': 30, 'bd': 3}

    acoes = [
        ('Sobreviventes/Mortos', 1),
        ('Porcentagem Mortos Maior de Idade', 2),
        ('Mortos por Classe', 3),
        ('Quantidade de Cônjuges', 4),
        ('Locais de Embarque', 5),
        ('Tarifas Pagas', 6),
        ('Relação Idade/Sobreviventes', 7),
        ('Total de Parentes', 8),
        ('Sobreviventes por gênero', 9),
        ('Média de preços por classe', 10)
    ]

    for idx, (acao, opcao) in enumerate(acoes):
        botao = tk.Button(janela, text=acao,
                          command=lambda opcao=opcao: executar_acao(opcao),
                          **estilo_botao)
        botao.grid(row=idx // 2, column=idx % 2, padx=5, pady=5)

    janela.mainloop()


criar_janela()
