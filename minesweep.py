#!/usr/bin/python

import os.path
import sys, getopt
from random import randint
import time

def randomer(tamanio,numMinas):
    celdaA = randint(0,tamanio)
    celdaB = randint(0,tamanio)
    return(celdaA,celdaB)

def initTablero(tamanio):
    #inicializa el tablero vacio
    tablero = [['0' for i in range(tamanio)] for i in range(tamanio)]
    return (tablero)

def minarTablero(numMinas,tamanio):
    #minare el tablero usando randomer
    tableroMinado = initTablero(tamanio)
    for i in range(numMinas):
        celdas =randomer(tamanio,numMinas)
        tableroMinado[celdas[0]][celdas[1]] = '1' #pongo unos?
    return tableroMinado

def getVecinos(tableroMinado,fila,columna):
    #me permite saber cuantas minas pueden llega a haber en torno al
    #casillero elegido
    #TODO, terminar funcion (Me fui a la facultad)
    vecinos =[] #estos seran puntos (f,c)
    for (fila-1) in range (fila+1):
        for (columna -1) in range (columna +1):
            if (fila-1) == 0 and (columna -1) == 0:
                continue
        elif tableroMinado[f][c] == 1:
            vecinos.append((f,c))
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

if __name__ == '__main__':
    #tamanio = input('Ingrese tamanio (0..9)')
    #minas = input('Ingrese cantidad de minas')
    #jugar(minas, tamanio)
    jugar(3,6)
