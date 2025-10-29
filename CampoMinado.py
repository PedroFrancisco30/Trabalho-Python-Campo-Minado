import random

def mostrar_mapa(mapa):
    """Mostra o campo de maneira organizada"""
    for linha in mapa:
        print(' '.join(linha))
    print()

MAX = 10

def minas_aleatorias(mapa,qtd_minas,simbolo = '#'):
    """Colocando as minas no mapa de maneira aleatoria"""
    linhas = len(mapa)
    colunas = len(mapa[0])
    if qtd_minas > linhas*colunas:
        print("Mais minas que espaços disponiveis")

    colocadas = 0
    #colocando as minas de maneira aleatoria ao longo do campo
    while colocadas < qtd_minas:
        lin = random.randrange(linhas)
        col = random.randrange(colunas)
        if mapa[lin][col] == '.':
            mapa[lin][col] = simbolo
            colocadas += 1
            
def contando_minas_vizinhas(mapa,lin,col):
    """Contando as minas em volta da posição clicada"""
    linhas = len(mapa)
    colunas = len(mapa[0])
    contagem = 0
    
    #contando se nas casas vizinhas existem minas e somando
    for i in range(lin-1,lin+2):
        for l in range(col-1,col+2):
            if 0 <= i < linhas and 0 <= l < colunas:
                if mapa[i][l] == '#':
                    contagem += 1
    return contagem

def abrindo_casas(campo_visivel, campo_real, lin, col):
    """Abrindo as casas perto da posição clicada"""
    linhas = len(campo_real)
    colunas = len(campo_real[0])

    if campo_visivel[lin][col] != '*':
        return True

    if campo_real[lin][col] == '#':
        return False  # pisou em bomba
    
    minas_viz = contando_minas_vizinhas(campo_real, lin, col)
    
    if minas_viz == 0:
        campo_visivel[lin][col] = ' ' # Mostra espaço em vez de '0'
    else:
        campo_visivel[lin][col] = str(minas_viz)
  
    #if que vai abrir todas as casas adjacentes que nao tiverem bomba
    if minas_viz == 0:
        for i in range(lin - 1, lin + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < linhas and 0 <= j < colunas:
                    if campo_visivel[i][j] == '*':
                        abrindo_casas(campo_visivel, campo_real, i, j)
    return True

def conferir_bomba(campo_real,campo_visivel):
    
    """Retorna True se o jogador ganhou o jogo."""
    for i in range(len(campo_real)):
        for j in range(len(campo_real[0])):
            if campo_real[i][j] == '#':  # é uma mina real
                if campo_visivel[i][j] != 'M':  # e não foi marcada
                    return False
            else:  # não é mina
                if campo_visivel[i][j] == 'M':  # marcou incorretamente
                    return False
    return True

def conferir_vitoria_por_abrir(campo_real, campo_visivel):
    """Retorna True se todas as casas seguras foram abertas."""
    linhas = len(campo_real)
    colunas = len(campo_real[0])
    
    for i in range(linhas):
        for j in range(colunas):
            # Se uma casa NÃO é bomba E ainda está fechada ('*')
            if campo_real[i][j] != '#' and campo_visivel[i][j] == '*':
                return False # Jogo não acabou
    
    return True
    
while True:

    try:
        linhas = int(input("Digite a quantidade de linhas do seu mapa: "))

        if (linhas < 4 or linhas > MAX):
            print("Numero invalido de linhas deve estar entre 4 e 10")
        else:
            break
    except ValueError:
        print("Digite apenas numeros")
    
while True:
    try:
        colunas = int(input("Digite a quantidade de colunas do seu mapa: "))

        if (colunas < 4 or colunas > MAX):
            print("Numero invalido deve estar entre 4 e 10")
        else:
            break
    except ValueError:
        print("Digite apenas numeros")

while True:
    try:
        max_bombas = linhas * colunas - 2

        qtd_bombas = int(input(f"Quantas bombas deseja adicionar?Maximo({max_bombas}) "))

        if (qtd_bombas > max_bombas or qtd_bombas < 0):
            print(f"Numero invalido! Voce pode escolher entre 0 e {max_bombas} robos.\n")
        else:
            break
    except ValueError:
        print("Digite apenas numeros")            

#Criando o campo original    
campo = []
    
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append('.')
    campo.append(linha)
     
#Criando o campo falso
campo_falso = []
    
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append('*')
    campo_falso.append(linha)
    
#Colocando as minas aleatorias e mostrando o campo falso    

minas_aleatorias(campo,qtd_bombas,'#')

print(" ")     
print("---Campo Minado---")
mostrar_mapa(campo_falso)

jogo = True
    
while jogo:
    
    print("--1)Marcar o mapa")
    print("--2)Abrir posicao no mapa")
    try:
        opcao = int(input("Qual opcao voce quer?"))
        print("")
        print("")
    except ValueError:
        print("Digite apenas numeros")
        continue
    match opcao:

        case 1:
            try:
                lin_marc = int(input("Qual linha voce quer marcar que tem uma bomba?"))-1
                col_marc = int(input("Qual coluna voce quer marcar que tem uma bomba?"))-1
                print("")
                print("")
                
                if(lin_marc < 0 or lin_marc >= linhas or col_marc < 0 or col_marc >= colunas):
                    print("Posicao fora do mapa")
                    continue
            except ValueError:
                print("Digite apenas numeros")
                continue
        
            campo_falso[lin_marc][col_marc] = 'M'

            mostrar_mapa(campo_falso)
            print(" ")
            print(" ")
    
        case 2:
            
            try:
                lin_abrir = int(input("Qual linha voce quer abrir?"))-1
                col_abrir = int(input("Qual coluna voce quer abrir?"))-1
                print("")
                print("")

                if(lin_abrir < 0 or lin_abrir >= linhas or col_abrir < 0 or col_abrir >= colunas):
                    print("Posicao fora do mapa")
                    continue
            except ValueError:
                print("Digite apenas numeros")
                continue
                
                
            if campo[lin_abrir][col_abrir] == '#':
                print("BOOOOOOOOMMMM")
                print("Voce perdeu!")
                break
                
            elif campo[lin_abrir][col_abrir] == '.':
                
                abrindo_casas(campo_falso,campo,lin_abrir,col_abrir)
                
                mostrar_mapa(campo_falso)
        case _:
            print("Opcao Invalida")
                
    vitoria_marcacao = conferir_bomba(campo, campo_falso)
    vitoria_abertura = conferir_vitoria_por_abrir(campo, campo_falso)

    if vitoria_marcacao or vitoria_abertura:
        print("---------------------------------")
        print("Parabens, voce limpou o campo!")
        print("VITORIA!")
        print("---------------------------------")
        mostrar_mapa(campo) 
        break 
