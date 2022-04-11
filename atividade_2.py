import os
import time
#-------------------------------------------------

#--------------  Algoritmo 88  -------------------

#-------------------------------------------------

def calculator():
  print ("\tfunction calculator:\n")
  print ("choice a operator for working")
  escolha = input("1-sum\n2-subtraction\n3-multiplication\n4-division\n")
  os.system("clear" if os.name == "posix" else "cls")
  n1=int(input("insert first number\n"))
  n2 = int(input("insert second number\n"))
  os.system("clear" if os.name == "posix" else "cls")
  if(escolha == '1'):
    print ("\nresult of the sum =", n1+n2)
  elif (escolha == '2'):
    print ("\nresult of the subtraction = ",n1-n2)
  elif (escolha == '3'):
    print ("\nresult of the multiplication = ",n1*n2)
  elif (escolha == '4'):
    print ("\nresult of the division = ",n1//n2,"and rest = ",n1%n2)
  else:
    print("invalid selected option")
  time.sleep(5)
  os.system("cls" if os.name == "nt" else "clear")
  

#-------------------------------------------------

#--------------  Algoritmo 97  -------------------

#-------------------------------------------------
def divisivel():
  print ("\tfunction if number is divisible by 10, 5, 2:\n")
  n1 = int(input("insert a number:\n"))
  if ((n1%10 == 0)):
    print("this number is divisible by 10 ")
    if ((n1%5 == 0)):
      print("this number is divisible by 5")
    if ((n1%2 == 0)):
      print("this number is divisible by 2 ")
  elif ((n1%5 == 0)):
    print("this number is divisible by 5")
    if ((n1%2 == 0)):
      print("this number is divisible by 2 ")
  elif ((n1%2 == 0)):
    print("this number is divisible by 2")
  else:
    print ("this number is not divisible by any number")
  time.sleep(5)
  os.system("cls" if os.name == "nt" else "clear")

#-------------------------------------------------

#--------------  Algoritmo 100  ------------------

#-------------------------------------------------
def multiploDe4():
  print ("\tfunction if number of 4 algarism is multiple of 4:\n")

  num = int(input("insert number:\n"))
  c = num / 100
  if (c%4 == 0):
    print("number is multiple of 4\n")
  else:
    print("number no is multiple of 4")
  time.sleep(5)
  os.system("cls" if os.name == "nt" else "clear")

#-------------------------------------------------

#--------------  Algoritmo 108  ------------------

#-------------------------------------------------
def nome():
  print ("\tfunction if name == josé:\n")
  nome = input("your name:\n")
  if (nome == 'josé' or nome == 'José' or nome == 'JOSÉ'):
    print (nome)
  time.sleep(5)
  os.system("cls" if os.name == "nt" else "clear")
#-------------------------------------------------

#--------------  Algoritmo 119  ------------------

#-------------------------------------------------
def ordem():
  print ("\tfunction descending order:\n")
  aux = int
  a = int(input("insert first number\n"))
  b = int(input("insert second number\n"))
  c = int(input("insert third number\n"))
  if (a > b):
    aux = a
    a = b
    b = aux
  if(a > c):
    aux =a
    a = c
    c = aux
  if (b > c):
    aux = b
    b = c
    c = aux
  print ("The descending order is:\n{}\n{}\n{}".format(c,b,a))
  time.sleep(5)
  os.system("cls" if os.name == "nt" else "clear")
#-------------------------------------------------

#--------------  Algoritmo 122  ------------------

#-------------------------------------------------
def ladosTriangulos():
  print ("\tif numbers can be triangles")
  l1 = int (input("insert first side:\n"))
  l2 = int (input("insert second side:\n"))
  l3 = int (input("insert third side:\n"))
  if (l1 < l2+l3 and l2<l1+l3 and l3 < l1+l2):
    print ("can be sides of a triangle:\n")
  else:
    print ("no can be side of triangle:\n")
  time.sleep(5)
  os.system("cls" if os.name == "nt" else "clear")
#-------------------------------------------------

#--------------  Algoritmo 123  ------------------

#-------------------------------------------------
def tipoDeTrinagulo():  
  print("\tfunction type of triangle")
  l1 = int (input("insert first side:\n"))
  l2 = int (input("insert second side:\n"))
  l3 = int (input("insert third side:\n"))
  if (l1 < l2+l3 and l2<l1+l3 and l3 < l1+l2):
    if(l1 == l2 and l1 == l3):
      print("this is a equilater triangle:\n")
    elif(l1 == l2 or l1 == l3 or l2 == l3):
      print("this is an isosceles triangle:\n")
    elif(l1 != l2 and l1 != l3 and l2 != l3):
      print("this is a scalene triangle:\n")
  else:
    print("measurements do not form a triangle:\n")
  time.sleep(5)
  os.system("cls" if os.name == "nt" else "clear")
#-------------------------------------------------

#--------------  Algoritmo 124  ------------------

#-------------------------------------------------
def classeDeTriangulo():
  print("\tclassification of triangle:\n")
  maior = int
  lados = int
  l1 = int (input("insert first side:\n"))
  l2 = int (input("insert second side:\n"))
  l3 = int (input("insert third side:\n"))
  if (l1 < l2+l3 and l2<l1+l3 and l3 < l1+l2):
    if(l1 > l2 and l1 > l3):
      maior = l1 ** 2
      lados = l2 ** 2 + l3**2
    elif(l2>l3):
      maior = l2**2
      lados = l1**2+l3**2
    else:
      maior = l3**2
      lados = l1**2+l2**2
    if (maior == lados ):
      print ("rectangle triangle:\n")
    elif(maior > lados):
      print ("obtuse triangle:\n")
    else:
      print ("acute triangle:\n")
  else:
    print ("measurements do not form a triangle")
  time.sleep(5)
  os.system("cls" if os.name == "nt" else "clear")
#-------------------------------------------------

#--------------  Algoritmo 138  ------------------

#-------------------------------------------------
def mes():
  print("\t if number is a month:\n")
  m = int(input("insert number:\n"))
  list=['January','February','March','April','May','June','July','August','September','October','November','December']
  print ("month does no exist" if ( m < 1 or m > 12) else list[m-1])
  time.sleep(5)
  os.system("cls" if os.name == "nt" else "clear")


calculator()
divisivel()
multiploDe4()
nome()
ordem()
ladosTriangulos()
tipoDeTrinagulo()
classeDeTriangulo()
mes()