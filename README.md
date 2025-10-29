# Campo Minado(Python)

Este é um jogo de Campo Minado simples que programei, desenvolvido em Python e jogado diretamente no terminal. O jogador define o tamanho do tabuleiro e o número de minas, e o objetivo é encontrar todas as minas sem detonar nenhuma.

##  Funcionalidades
* Tabuleiro Customizável: O jogador pode escolher o número de linhas e colunas (mínimo de 4x4, máximo de 10x10).
* Dificuldade Ajustável: O jogador define quantas minas estarão escondidas no campo.
* Lógica de Abertura Recursiva: Ao abrir uma casa que não possui minas vizinhas, o jogo automaticamente revela todas as casas seguras adjacentes (conhecido como flood fill).

## Duas Formas de Vencer:
* Marcando corretamente todas as posições com minas (com a letra 'M').
* Abrindo todas as casas que não possuem minas.

## Como Executar
    Para jogar, você precisa ter o Python 3 instalado em sua máquina, ai é necessario baixar o arquivo CampoMinado.py,abrir o terminal e navegar ate o diretorio do arquivo e tem que executar o script com Bash python CampoMinado.py

### Como jogar

    • Ao iniciar, o programa solicitará que você defina:
        A quantidade de linhas do Mapa
        A quantidade de colunas do Mapa
        A quantidade de bombas que deseja adicionar

    • Em cada rodada,voce tera duas opções:
        1) Marcar o mapa: Use esta opção para marcar uma casa que você suspeita conter uma mina. Ela será exibida com um M.
        2) Abrir posicao no mapa: Use esta opção para revelar o conteúdo de uma casa.


| Ao cliclar em uma          | Resultado                                                | 
| :-------------------------:| :-------------------------------------------------------:|
|   MINA                     | Voce perde o jogo(BOOOM)                                 | 
|   CASA SEGURA              | Mostra o numero de minas existentes nas 8 casas vizinhas | 
|   CASA SEGURA(0 MINAS)     | Jogo abre automaticamente as casas ao redor              | 


## Condições de Vitória e Derrota

  ### Vitória
```
* O jogador vence ao conseguir marcar com M todas as posições que possuem Minas
* O jogador conseguir abrir todas casas seguras(que nao contêm minas)
```

### Derrota
```bash
* Abrir uma posição que contém uma mina.
```

## Descrição Final

Este projeto utiliza apenas bibliotecas padrão do Python, sem necessidade de instalação de pacotes externos.

random (para a geração aleatória das minas)
