import numpy as np
import math 


'''
Esse código foi feito Por Rafael Ribeiro, Facilitador da disciplina Algoritmos e Programação de Computadores I

Aqui terá esritas funções que, serão usadas durante os exercícios durante a semana.

Os exercícios são tirados do livro : Introduçao a Computacão com Python  PERKOVIC, Ljubomir
'''

############################################Exercício do cap 3 do livro#############################################################################
####################################################################################################################################################

#3.1

def temp_C(t):
    celsius = (5/9)*(t-32)
    return celsius

# 3.2

def media(n1,n2): # tem como fazer uma funcão media para qualquer númedo de dados? A cargo de leitor
    return (n1+n2)/2

#3.9

def perimeter(r):
    if r<0:
        print("ERRO!\nNão existe raio negativo")
        return None
    else 
        per = 2*math.pi*r
        return per

#3.10

def count_n(l):
    l = l.sort()
    for i in range(len(l)):
        if l[i]<0:
            print(l[i],"/n")

#3.11

def media_2(x,y):
    'retorna a média de x e y'
    return (n1+n2)/2

#3.13

def invert_list(l):
    aux_1 = l[-1]
    aux_2 = l[0]
    l[0] = aux_1
    l[-1] = aux_2
    return l

#3.14

def trocarPU(l):
    if len(a) == 0:
        print('Lista Vazia!')
        return None
    # Eu fiz dois jeitos de fazer isso, será que tem mais?
    #if a == []:
        #print('Lista Vazia!')
        #return None
    aux_1 = l[-1]
    aux_2 = l[0]
    l[0] = aux_1
    l[-1] = aux_2
