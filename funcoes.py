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


def quantidadeDeConjulgues():
    parchs = {}

    for x in tit:
        parch = x['Parch']
        if parch not in parchs:
            parchs[parch] = 1
        else:
            parchs[parch] += 1

    valores_parch = list(parchs.keys())
    quantidade_pessoas = list(parchs.values())

    plt.bar(valores_parch, quantidade_pessoas)
    plt.xlabel('Quantidade de cônjulgues')
    plt.ylabel('Quantidade de pessoas')
    plt.title('Quantidade de pessoas por quantidade de cônjulgues')
    plt.show()


def locaisDeEmbarque():
    locais = {}

    for x in tit:
        loc = x['Embarked']
        if loc not in locais:
            locais[loc] = 1
        else:
            locais[loc] += 1

    embarcacoes = list(locais.keys())
    pessoasPorLocal = list(locais.values())

    plt.bar(embarcacoes, pessoasPorLocal)
    plt.xlabel('Locais de embarque')
    plt.ylabel('Quantidade de pessoas que embarcaram')
    plt.title('Quantidade de pessoas que embarcaram em cada lugar')
    plt.show()


def tarifasPagas():
    tarifas = []

    for passageiro in tit:
        fare = passageiro['Fare']
        if fare:
            try:
                tarifa = float(fare)
                tarifas.append(tarifa)
            except ValueError:
                pass

    plt.figure(figsize=(8, 6))
    plt.hist(tarifas, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Tarifa')
    plt.ylabel('Frequência')
    plt.title('Distribuição das Tarifas Pagas pelos Passageiros')
    plt.grid(True)
    plt.show()


def relacaoIdadeSobreviventes():
    idades_sobreviventes = []
    idades_mortos = []

    for passageiro in tit:
        idade = passageiro['Age']
        if idade != '':
            if passageiro['Survived'] == '1':
                idades_sobreviventes.append(float(idade))
            else:
                idades_mortos.append(float(idade))

    plt.figure(figsize=(8, 6))
    plt.boxplot([idades_sobreviventes, idades_mortos],
                labels=['Sobreviventes', 'Mortos'])
    plt.xlabel('Status')
    plt.ylabel('Idade')
    plt.title('Comparação de Idades entre Sobreviventes e Mortos')
    plt.grid(True)
    plt.show()


def totalDeParentes():
    total_parentes = []

    for x in tit:
        sibsp = int(x['SibSp'])
        parch = int(x['Parch'])
        total_parentes.append(sibsp + parch)

    plt.figure(figsize=(8, 6))
    plt.hist(total_parentes, bins=max(total_parentes) -
             min(total_parentes), color='green', edgecolor='black')
    plt.xlabel('Número Total de Parentes a Bordo')
    plt.ylabel('Frequência')
    plt.title('Distribuição do Número Total de Parentes a Bordo')
    plt.show()


def sobreviventesPorGenero():
        mulher = 0
        homem = 0

        for x in tit:
            if x['Survived'] == '1' and x['Sex'] == 'female':
                mulher += 1
            elif x['Survived'] == '1' and x['Sex'] == 'male':
                homem += 1

        y = [homem, mulher]
        legendas = [f"Sobrevientes homens: {str(homem)}", f"Sobreviventes mulheres: {str(mulher)}"]

        plt.title('Números de sobreviventes por gênero')
        plt.pie(y, labels=legendas)
        plt.show()


def mediaPrecosPorClasse():
    classe1 = []
    classe2 = []
    classe3 = []


    for passageiro in tit:
        classe = int(passageiro['Pclass'])
        fare = float(passageiro['Fare'])
        
        if classe == 1:
            classe1.append(fare)
        elif classe == 2:
            classe2.append(fare)
        elif classe == 3:
            classe3.append(fare)

    media_classe1 = sum(classe1) / len(classe1) if classe1 else 0
    media_classe2 = sum(classe2) / len(classe2) if classe2 else 0
    media_classe3 = sum(classe3) / len(classe3) if classe3 else 0

    classes = [media_classe1, media_classe2, media_classe3]
    legendas = ["Classe 1", "Classe 2", "Classe 3"]

    plt.title("Média de Preços por Classe")
    plt.bar(legendas, classes, color=['blue', 'orange', 'green'])
    plt.xlabel("Classes dos Passageiros")
    plt.ylabel("Média de Preços")
    plt.show()

