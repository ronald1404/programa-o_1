import random
random.seed();

dados = int(input("escolhas quantos dados quer rolar:\n"))
faces = int(input("quantas faces tem cada dado: 4, 6, 8, 10, 12, 20\n"))
roladas = int(input("roladas:\n"))

contador = 0
somaDados = 0
while contador <dados: 
    sorteio = random.randint(1,faces); 
    print (contador+1,"° dado:",sorteio)
    somaDados+=sorteio
    contador+=1

print("o resulta final da soma dos dados foi", somaDados)