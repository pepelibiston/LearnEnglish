import random
import sys

SECUENCIAL = 1
RANDOM = 2

ALIMENTOS = 1
ROPA = 2
FOODACTION= 3
SINONIMOS= 4
#Gestiona este conflicto men
vocabulariosTipo = ["Alimentos", "Ropa", "Acciones comida", "Sinonimos"]
ficherosVocabulario = ["alimentos.txt", "ropa.txt", "foodAction.txt","sinonimos.txt"]

class Vocabulary:
    def __init__(self, vocabulario):
        self.vocabulariotxt = vocabulario
        self.espanol = []
        self.ingles = []
        self.sinonimo = []
        self.modo = -1

    def procesarLinea(self, linea):
        procesado = linea.split(';')
        self.espanol.append(procesado[0])
        self.ingles.append(procesado[1])

    def procesarLineaS(self, linea):
        procesado = linea.split(';')
        self.espanol.append(procesado[0])
        self.ingles.append(procesado[1])
        self.sinonimo.append(procesado[2])

    def cargarVocabulario(self, sinonimo):
        f = open(self.vocabulariotxt)
        if sinonimo != 1:
            for linea in f:
                self.procesarLinea(linea)
        else:
            for linea in f:
                self.procesarLineaS(linea)
        f.close()


    def verificar(self, pos):
        respuesta = input(">> " + self.espanol[pos] + ": ")
        correcto = self.ingles[pos]
        if str(respuesta) == str(correcto):
            print("[+]")
        else:
            print("[-] -> " + correcto)

    def verificarS(self,pos):
        respuesta1 = input(">> " + self.espanol[pos] + ": ")
        respuesta2 = input(">> " + self.espanol[pos] + ": ")
        correcto1 = self.ingles[pos]
        correcto2 = self.sinonimo[pos]
        cond1 = str(respuesta1) == str(correcto1) or str(respuesta1) == str(correcto2)
        cond2 = str(respuesta2) == str(correcto1) or str(respuesta2) == str(correcto2)
        if cond1 and cond2:
            print("[+]")
        else:
            print("[-] -> " + correcto1 + ", " + correcto2)

    def run(self):
        modo = input("Introduce modo de juego:\n\t[1] secuencial\n\t[2] random\n")
        if int(modo) == int(SECUENCIAL):
            numPalabras = len(self.espanol)
            contador = 0
            while contador < numPalabras:
                self.verificar(contador)
                contador += 1
        else:
            while True:
                x = random.randint(0,len(self.espanol)-1)
                self.verificar(x)

    def runS(self):
        modo = input("Introduce modo de juego:\n\t[1] secuencial\n\t[2] random\n")
        if int(modo) == int(SECUENCIAL):
            numPalabras = len(self.espanol)
            contador = 0
            while contador < numPalabras:
                self.verificarS(contador)
                contador += 1
        else:
            while True:
                x = random.randint(0,len(self.espanol)-1)
                self.verificar(x)

print("¿Que te apetece estudiar hoy?")
contador = 1
sinonimos = -1
for i in vocabulariosTipo:
    print("\t[" + str(contador) + "]" + i)
    contador += 1

tema = input()
if int(tema) == int(ALIMENTOS):
    aptis = Vocabulary("alimentos.txt")
elif int(tema) == int(ROPA):
    aptis = Vocabulary("ropa.txt")
elif int(tema) == int(FOODACTION):
    aptis = Vocabulary("foodAction.txt")
else:
    aptis = Vocabulary("sinonimos.txt")
    sinonimos = 1

if sinonimos != 1:
    aptis.cargarVocabulario(sinonimos)
    aptis.run()
else:
    aptis.cargarVocabulario(sinonimos)
    aptis.runS()
