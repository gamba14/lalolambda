#!/usr/bin/python

import os.path
import sys, getopt
from random import randint
import time
import string

def randomer(tamanio,numMinas):
    celdaA = randint(1,tamanio-1) #a veces fallaba con 0,tamanio
    celdaB = randint(1,tamanio-1) #ahora no, siempre devuelve un tablero
    return(celdaA,celdaB)

def initTablero(tamanio):
    #inicializa el tablero vacio
    tablero = [[0 for i in range(tamanio)] for i in range(tamanio)]
    return (tablero)

def minarTablero(numMinas,tamanio):
    #minare el tablero usando randomer
    tableroMinado = initTablero(tamanio)
    for i in range(numMinas):
        celdas =randomer(tamanio,numMinas)
        tableroMinado[celdas[0]][celdas[1]] = 1 #pongo unos?
    return tableroMinado

def getVecinos(tableroMinado,f,c):
    #me permite saber cuantas minas pueden llega a haber en torno al
    #casillero elegido
    vecinos =[] #estos seran puntos (f,c)
    if tableroMinado[f][c] != 1:
        for i in range (-1,2):
            for j in range (-1,2):
                if tableroMinado[f+i][c+j] == 1:
                    vecinos.append((f+i,c+j))
    return vecinos
def descubrirMina(tableroMinado,tablero,f,c):
    if tableroMinado[f][c] == 1:
        print('BOOOOOOOOOOOOOOOOOOM\n')
        jugarNuevo()
    else:
        vecinos = getVecinos(tableroMinado,f,c)
        tablero[f][c]= len(vecinos)
        for i in vecinos:
            if tableroMinado[i[0]][i[1]] != 1:
                tablero[i[0]][i[1]]=-1
    return tablero
def jugarNuevo():
    continuar=input('Jugar de nuevo?(s/n)\n')
    if continuar.lower() == 's':
        return True
    else:
        return False

def mostrarTablero(tableroMinado):
    #os.system('clear')
    tamanio = len(tableroMinado)
    #imprimo una linea horizontal del ancho de la grilla
    horizontal = '   ' + (4 * tamanio * '-') + '-'
    print(horizontal)
    for i in enumerate(tableroMinado):
        print(i)
    print(horizontal)
def parseInput():
    dictCo={'a':0,'b':1,'c':2,'d':3,'e':4}
    cor = input('>ingrese coordenada. ')
    corList = list(cor)
    corListPar=(dictCo[corList[0]],int(corList[1]))
    return corListPar

#Jugar funcion que me permite basicamente jugar
def jugar(minas, tamanio,tablero):
    perdiste = False
    tableroMinado = minarTablero(minas,tamanio)
    while not perdiste:
        coordenada=parseInput()
        tablero = descubrirMina(tableroMinado,tablero,coordenada[0],coordenada[1])
        mostrarTablero(tableroMinado)
        vecinos = getVecinos(tableroMinado,3,3)
        print(vecinos)
        mostrarTablero(tablero)

if __name__ == '__main__':
    #tamanio = input('Ingrese tamanio (0..9)')
    #minas = input('Ingrese cantidad de minas')
    #jugar(minas, tamanio)
    tablero=initTablero(6)
    jugar(10,6,tablero)
