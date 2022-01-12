# Davi Ferreira do Vale
####

import os
import random
from colorama import Fore

jogarNovamente = "s"
moves = 0
quemJoga = 2
maxJogadas = 9
vencedor = ""
matriz = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def tela():
    global matriz
    global moves
    os.system("cls")
    print("     1    2    3")
    print("1:    " + matriz[0][0] + " | " + matriz[0][1] + " | "+ matriz[0][2])
    print("    -------------")
    print("2:    " + matriz[1][0] + " | " + matriz[1][1] + " | "+ matriz[1][2])
    print("    -------------")
    print("3:    " + matriz[2][0] + " | " + matriz[2][1] + " | "+ matriz[2][2])
    print("Moves: " + Fore.GREEN + str(moves) + Fore.RESET)

def jogadorJoga():
    global moves
    global quemJoga
    global maxJogadas

    if quemJoga == 2 and moves < maxJogadas:
        l = int(input("Linha..: "))
        l = l-1

        c = int(input("Coluna.: "))
        c = c-1
        
        try:    
            while matriz[l][c] != " ":
                l = int(input("Linha..: "))
                l = l-1

                c = int(input("Coluna.: "))
                c = c-1

            matriz[l][c] = "X"
            quemJoga = 1
            moves+=1
        except:
            print("Espaço inválido!")

def cpuJoga():
    global moves
    global maxJogadas
    global quemJoga

    if quemJoga == 1 and moves < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)

        while matriz [l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        
        matriz[l][c] = "O"
        quemJoga = 2
        moves+=1

def verificarVitoria():
    global matriz
    vitoria = "n"
    simbolos = ["X", "O"]

    for s in simbolos:
        vitoria = "n"
        il = ic = 0

        #verifica linhas
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if(matriz[il][ic] == s):
                    soma+=1
                ic+=1
            if(soma == 3):
                vitoria = s
                break
            il += 1

        if(vitoria != "n"):
            break

        #verifica colunas
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if(matriz[il][ic] == s):
                    soma+=1
                il+=1
            if(soma == 3):
                vitoria = s
                break
            ic += 1

        if(vitoria != "n"):
            break

        #verifica diagonal e-d
        soma = 0
        idiag = 0

        while idiag <3:
            if(matriz[idiag][idiag] == s):
                soma+=1
            idiag += 1
        if(soma == 3):
            vitoria = s
            break

        #verifica diagonal d-e
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if(matriz[idiagl][idiagc] == s):
                soma+=1
            idiagl += 1
            idiagc -= 1
        if(soma == 3):
            vitoria = s
            break
    return vitoria
        #verifica diagonal d-e

def redefinir():
    global matriz
    global moves
    global quemJoga
    global maxJogadas
    global vencedor
    moves = 0
    quemJoga = 2 #1 = CPU | #2 = Jogador
    maxJogadas = 9
    vencedor = ""
    matriz = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]


while(jogarNovamente == "s"):
    while True:
        tela()
        jogadorJoga()
        cpuJoga()
        vencedor = verificarVitoria()
        if(vencedor != "n") or (moves >= maxJogadas):
            break

    print(Fore.RED + "Finish" + Fore.YELLOW)
    if vencedor == "X":
        print("You win!!!")
    elif vencedor == "O":
        print("A CPU venceu")
    else:
        print("Resultado: Empate")
    jogarNovamente = input(Fore.BLUE + "Digite [s] para continuar ou [n] para sair: " + Fore.RESET)
    redefinir()

