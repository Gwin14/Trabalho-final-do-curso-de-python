import json
import matplotlib.pyplot as plt

tit = json.load(open("titanic.json", "r"))


def sobrevientesMortos():
    sobrevivido = 0
    morto = 0

    for x in tit:
        if x['Survived'] == '1':
            sobrevivido += 1
        else:
            morto += 1

    y = [sobrevivido, morto]
    legendas = [f"Sobrevientes: {str(sobrevivido)}", f"Mortos: {str(morto)}"]

    plt.title('Números de sobreviventes e mortos do titanic')
    plt.pie(y, labels=legendas)
    plt.show()


def porcentagemMortosMaiorDeIdade():
    mortosMaior = 0
    mortosMenor = 0

    totalMortos = 0
    naoIdentificados = 0

    for x in tit:
        if x['Age'] != '' and x['Survived'] == '0':
            if float(x['Age']) < 18:
                mortosMenor += 1
                totalMortos += 1
            else:
                mortosMaior += 1
                totalMortos += 1
        if x['Age'] == '':
            naoIdentificados += 1

    mortos = [mortosMaior, mortosMenor]
    porcentagemDeMenor = round(mortosMenor/totalMortos * 100)
    porcentagemDeMaior = round(mortosMaior/totalMortos * 100)

    legendas = [
        f'Vítimas maior de idade: {porcentagemDeMaior}%', f'Vítimas menor de idade: {porcentagemDeMenor}%']

    plt.title(
        f'Porcentagem de vítimas por idade, ({naoIdentificados} pessoas não tiveram idade identificada)')
    plt.pie(mortos, labels=legendas)
    plt.show()


def mortosPorClasse():
    tit = json.load(open("titanic.json", "r"))

    classe1 = 0
    classe2 = 0
    classe3 = 0

    for x in tit:
        if x['Pclass'] == '1' and x['Survived'] != '1':
            classe1 += 1
        if x['Pclass'] == '2' and x['Survived'] != '1':
            classe2 += 1
        if x['Pclass'] == '3' and x['Survived'] != '1':
            classe3 += 1

    classes = [classe1, classe2, classe3]
    legendas = ["Classe 1", "Classe 2", "Classe 3"]

    plt.title("Passageiros mortos por classe")
    plt.bar(legendas, classes)
    plt.xlabel("Classes dos passageiros")
    plt.ylabel("Quantidade de Mortes")
    plt.show()
