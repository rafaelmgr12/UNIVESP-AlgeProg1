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
    c = input("Digite a temperatura atual em graus Fahrenheit:\n") 
    t = float(c)
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
    else:
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

def trocaPU(l):
    if len(l) == 0:
        print('Lista Vazia!\n')
        return None
    # Eu fiz dois jeitos de fazer isso, será que tem mais?
    #if l == []:
        #print('Lista Vazia!')
        #return None
    aux_1 = l[-1]
    aux_2 = l[0]
    l[0] = aux_1
    l[-1] = aux_2

############################################Exercício da Semana 5#############################################################################
####################################################################################################################################################

### Olhar o Notebook da semana 5#################


def problema_3_2():
    #a)
    idade = eval(input("Digite sua Idade"))
    if idade > 62:
        print("Você pode obter benefícios de pensão")
    #b)
    
    jogadores = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
    nome = input("Digite um nome")
    if nome in jogadores:
        print("Um dos 5 maiores jogadores de beisebol de todos os tempos!")
    
    golpes = eval(input("O valor do golpe"))
    defesas = eval(input("O valor da defesa"))
    if golpes > 10 and defesas == 0:
        print("Você está morto")
    
    norte = True
    sul = False
    leste = False
    oeste = True
    if norte or sul or leste or oeste == True:
        print('Posso escapar.')


# 3.3)
def problema_3_3():
    #a)
    ano = eval(input("Digite um ano"))
    if ano % 4 == 0:
        print('Pode ser um ano bissexto.')
    else:
        print('Nãe é um ano bissexto.')

    #b) 
    print("Ós números da loteria é 1 número inteiros de 0 a 100\n\n--------------------------------\n\n")
    bilhete = eval(input("Digite os numeros do bilhete da seguinte forma:\n 15"))
    np.random.seed(10)
    loteria = np.random.randint(0,100,1)
    if bilhete == loteria:
        print('Você ganhou!')
    else:
        print('Melhor sorte da próxima vez...')

def problema_3_4():
    usuários = ['joe', 'sue', 'hani', 'sophie']
    id = input('Login: ')
    if id in usuários:
        print('Você entrou!')
    else:
        print('Usuário desconhecido. ')
    
    print('Fim.')

def meuIMC(peso, altura):
  'exibe relatório do IMC '
  imc = peso / altura**2
  if imc < 18.5:
    print('Abaixo do peso')
  elif imc < 25:
    print('Normal')
  else:                       # pode ser elif imc >= 25
    print('Sobbrepeso')




