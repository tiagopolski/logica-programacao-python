def entrevista():
    op = 1
    serie = -1
    idade = -1
    qtde = -1
    redacao = -1
    cont3ano = 0
    maior4ano = 0
    cont3anoN = 0
    cont12 = 0
    cIdade = 0
    while op != 0:
        while serie < 1 or serie > 4:
            serie = int(input('Informe a serie (1-4):'))
        while idade < 0:
            idade = int(input('Informe a idade:'))
        while qtde < 0:
            qtde = int(input('Quantidade de livros:'))
        while redacao < 0 or redacao > 1:
            redacao = int(input('Gosta de redacao 1-Sim 0-Nao '))
        if serie == 3:
            cont3ano = cont3ano + 1
            if redacao == 0:
                cont3anoN = cont3anoN + 1
        if serie == 4:
            if qtde > maior4ano:
                maior4ano = qtde
        if serie == 1 or serie == 2:
            cont12 = cont12 + 1
            cIdade = cIdade + idade
        serie = -1
        idade = -1
        qtde = -1
        redacao = -1
        op = int(input('Deseja sair 0-Sim 1-Nao '))
    print('Quantidade alunos 3 ano', cont3ano)
    print('O aluno do 4 ano que leu mais livros:', maior4ano)
    if cont3ano > 0:
        perc = (cont3anoN/cont3ano) * 100
        print('Percentual nao gosta de redacao do 3 ano', perc)
    if cont12 > 0:
        print('Media idade 1 e 2 anos:', cIdade / cont12)

#main
#entrevista()