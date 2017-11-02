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
