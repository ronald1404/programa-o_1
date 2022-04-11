import math
import os
import time

'''
cada algoritmo foi definido como uma função
ao final de cada função o usuário confirma a resposta no tempo de 5 segundos
ao final dos 5 segundos a tela ira limpar e uma nova função do algoritmo sera executada.

'''
#-------------------------------------------------

#--------------  Algoritmo 23  -------------------

#-------------------------------------------------
def dezena():
  num = int (input("digite um número de 3 algarimos\n"))
  dezenas = (num//10) % 10
  print (dezenas)
  time.sleep(5)
#-------------------------------------------------

#--------------  Algoritmo 25  -------------------

#-------------------------------------------------
def data():
  data = int(input("digite uma data no formato ddmmaa:\n"))
  dia = data // 10000
  mes = (data % 10000)//100
  ano = data % 100
  print ("dia {}, do mês {} do ano {}".format(dia,mes,ano))
  time.sleep(5)
#-------------------------------------------------

#--------------  Algoritmo 25  -------------------

#-------------------------------------------------
def sucessor_antecessor():
  num = int (input("digite um número:\n"))
  antecessor = num-1
  sucessor = num+1
  print ("o antecessor deste numero é :{}\no sucessor deste número é: {}".format(antecessor,sucessor))
  time.sleep(5)
#-------------------------------------------------

#--------------  Algoritmo 38  -------------------

#-------------------------------------------------
def terca_parte():
  n1 = float (input('entre com um numero com ponto:\npor exemplo: "3.0"\n'))
  print('a terça parte é: %1.2f' %(n1/3))
  time.sleep(5)

#-------------------------------------------------

#--------------  Algoritmo 39  -------------------

#-------------------------------------------------
def media_aritmetica():
  n1 = float (input("digite a primeira nota:\n"))
  n2 = float (input("digite a segunda nota:\n"))
  n3 = float (input("digite a terceira nota:\n"))
  print ('a media das notas é de %1.1f'%((n1+n2+n3)/3))
  time.sleep(5)

#-------------------------------------------------

#--------------  Algoritmo 40  -------------------

#-------------------------------------------------
def saida():
  dividendo = int(input("entre com o dividendo:\n"))
  divisor = int(input("entre com o divisor:\n"))
  quociente = int (dividendo /divisor)
  resto = dividendo % divisor
  print ("dividendo = {}\ndivisor = {}\nquociente = {}\nresto = {}".format(dividendo,divisor,quociente,resto))
  time.sleep(5)

#-------------------------------------------------

#--------------  Algoritmo 41  -------------------

#-------------------------------------------------
def media_ponderada():
  a = float(input("entre com o 1° número\n"))
  b = float(input("entre com o 2° número\n"))
  c = float(input("entre com o 3° número\n"))
  d = float(input("entre com o 4° número\n"))
  print ("a media pondera é = {}".format((a+b*2+c*3+d*4)/10))
  time.sleep(5)
#-------------------------------------------------

#--------------  Algoritmo 42  -------------------

#-------------------------------------------------
def angulos():
  angulo = int(input("digite o angulo em graus:\n"))
  rang = (angulo * math.pi)/180
  seno = math.sin(rang)
  cosseno = math.cos(rang)
  tangente = math.tan(rang)
  co_secante = 1/seno
  secante = 1/cosseno
  cotangente = 1 / tangente
  print("seno = {}\ncosseno ={}\ntangente = {}\nco-secante = {}\ncotangente = {}\n".format(seno,cosseno,tangente,co_secante,secante,cotangente))
  time.sleep(5)
#-------------------------------------------------

#--------------  Algoritmo 43  -------------------

#-------------------------------------------------
def logaritmo():
  num = int(input("digite um número:\n"))
  print ("o lagaritmo de {} na base 10 é = ".format(num),math.log(num,10))
  time.sleep(5)
#-------------------------------------------------

#--------------  Algoritmo 44  -------------------

#-------------------------------------------------

def logaritmo2():
  log = int(input("entre com o logaritmo:\n"))
  base = int(input("entre com a base:\n"))
  print ("o lagaritmo de {} na base {} é = ".format(log,base), math.log(log,base))
  time.sleep(5)

dezena()
os.system('cls' if os.name == 'nt' else 'clear')
data()
os.system('cls' if os.name == 'nt' else 'clear')
sucessor_antecessor()
os.system('cls' if os.name == 'nt' else 'clear')
terca_parte()
os.system('cls' if os.name == 'nt' else 'clear')
media_aritmetica()
os.system('cls' if os.name == 'nt' else 'clear')
saida()
os.system('cls' if os.name == 'nt' else 'clear')
media_ponderada()
os.system('cls' if os.name == 'nt' else 'clear')
angulos()
os.system('cls' if os.name == 'nt' else 'clear')
logaritmo()
os.system('cls' if os.name == 'nt' else 'clear')
logaritmo2()
os.system('cls' if os.name == 'nt' else 'clear')