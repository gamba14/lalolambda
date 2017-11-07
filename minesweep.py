#!/usr/bin/python

import os.path
import sys, getopt
from random import randint
import time

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

def mostrarTablero(tableroMinado):
    os.system('clear')
    tamanio = len(tableroMinado)
    #imprimo una linea horizontal del ancho de la grilla
    horizontal = '   ' + (4 * tamanio * '-') + '-'
    print(horizontal)
    for i in enumerate(tableroMinado):
        print(i)
    print(horizontal)

#Jugar funcion que me permite basicamente jugar
def jugar(minas, tamanio):
    perdiste = False
    tableroMinado = minarTablero(minas,tamanio)
    #while not perdiste:
    mostrarTablero(tableroMinado)
#    for i in range(len(tableroMinado)):
#        for j in range(len(tableroMinado)):
#            vecinos = getVecinos(tableroMinado,i,j)
    vecinos = getVecinos(tableroMinado,3,3)
    print(vecinos)

if __name__ == '__main__':
    #tamanio = input('Ingrese tamanio (0..9)')
    #minas = input('Ingrese cantidad de minas')
    #jugar(minas, tamanio)
    jugar(3,6)
