import numpy as np
import math 

#############################################################################################################
# Esse código foi feito Por Rafael Ribeiro, Facilitador da disciplina Algoritmos e Programação de 
# Computadores I
#
#
# Aqui terá esritas funções que, serão usadas durante os exercícios durante a semana.
#
# Os exercícios são tirados do livro : Introduçao a Computacão com Python  PERKOVIC, Ljubomir
#############################################################################################################

#########################################################################################################################
# Exercício do cap 3 do livro
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
    idade = eval(input("Digite sua Idade\n"))
    if idade > 62:
        print("Você pode obter benefícios de pensão\n")
    #b)
    
    jogadores = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
    nome = input("Digite um nome\n")
    if nome in jogadores:
        print("Um dos 5 maiores jogadores de beisebol de todos os tempos!\n")
    
    golpes = eval(input("O valor do golpe\n"))
    defesas = eval(input("O valor da defesa\n"))
    if golpes > 10 and defesas == 0:
        print("Você está morto\n")
    
    norte = True
    sul = False
    leste = False
    oeste = True
    if norte or sul or leste or oeste == True:
        print('Posso escapar.\n')


# 3.3)
def problema_3_3():
    #a)
    ano = eval(input("Digite um ano\n"))
    if ano % 4 == 0:
        print('Pode ser um ano bissexto.\n')
    else:
        print('Nãe é um ano bissexto.\n')

    #b) 
    print("O números da loteria é 1 número inteiro de 0 a 100\n\n--------------------------------\n\n")
    bilhete = eval(input("Digite os numeros do bilhete da seguinte forma:\n 15\n"))
    np.random.seed(10)
    loteria = np.random.randint(0,100,1)
    if bilhete == loteria[0]:
        print('Você ganhou!\n')
    else:
        print('Melhor sorte da próxima vez...\n')

def problema_3_4():
    usuários = ['joe', 'sue', 'hani', 'sophie']
    id = input('Login: ')
    if id in usuários:
        print('Você entrou! \n')
    else:
        print('Usuário desconhecido. \n')
    
    print('Fim.\n\n')

def meuIMC(peso, altura):
  'exibe relatório do IMC '
  imc = peso / altura**2
  if imc < 18.5:
    print('Abaixo do peso\n')
  elif imc < 25:
    print('Normal\n')
  else:                       # pode ser elif imc >= 25
    print('Sobrepeso\n')

############################################Exercício da Semana 6 #############################################################################
####################################################################################################################################################

### Olhar o Notebook da semana 6 #################


def problema_3_5():
    listaPalavras = eval(input("Digite a lista de palavras:"))
    for i in listaPalavras:
        if len(i) == 4 :
            print(i)

def problema_3_6():
   #a)
    for i in range(0,10):
        print('\n',i)
    #b)
    for i in range(2):
        print(i)

def problema_3_7():
    #a)
    for i in range(3,13):
        print("\n",i)
    for i in range(0,10,2):
        print("\n",i)
    for i in range(0,24,3):
        print("\n",i)
    for i in range(3,12,5):
        print("\n",i)

###################################################################
# Semana 7 - Olhar o notebook Semana_7.ipynb
###################################################################

# Exercio da aula

def transposta(l):
  tam = len(l)
  lt = [[0,0],[0,0]]
  for i in range(tam):
    for j in range(tam):
      lt[i][j] =l[j][i]
  return lt

def problema_4_1():
    s = '0123456789'
    print('a)\n\n',s[2:5])
    print('b)\n\n',s[7:9])
    print('c)\n\n', s[1:8])
    print('d)\n\n',s[:4])
    print('e)\n\n',s[7:])
    print('f)\n\n', s[-3:1])

def problema_4_2():
    forecast = 'It will be a sunny day today'
    cont = forecast.count('day')
    print ('a)\n\n',cont)
    clima = forecast.find('sunny')
    print ('b)\n\n',clima)
    troca = forecast.replace('sunny', 'cloudy')
    print ('c)\n\n',troca)

# Problema Prático 5_9
def soma2D(t1,t2):
    '''
    t1 e t2 são listas 2D com o mesmo número de linhas e mesmo número de colunas de 
    tamanho igual add2D incrementa cada item t1[i][j[ por t2[i][j]
    ''' 
    nlinhas = len(t1) # número de linhas 
    ncolunas = len(t1[0]) # número de colunas 
    for i in range(nlinhas): # para cada índice de linha i 
        for j in range(ncolunas): # para cada índice de coluna j 
            
            t1[i][j] += t2[i][j]
    return t1

