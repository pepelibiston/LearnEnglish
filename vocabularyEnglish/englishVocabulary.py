import random
import sys

SECUENCIAL = 1
RANDOM = 2

vocabulariosTipo = ["alimentos", "ropa"]
ficherosVocabulario = ["alimentos.txt"]

class Vocabulary:
    def __init__(self, vocabulario):
        self.vocabulariotxt = vocabulario
        self.espanol = []
        self.ingles = []
        self.modo = -1

    def procesarLinea(self, linea):
        procesado = linea.split(';')
        self.espanol.append(procesado[0])
        self.ingles.append(procesado[1])

    def cargarVocabulario(self):
        f = open(self.vocabulariotxt)
        for linea in f:
            self.procesarLinea(linea)
        f.close()

    def verificar(self, pos):
        respuesta = input(">> " + self.espanol[pos] + ": ")
        correcto = self.ingles[pos]
        if str(respuesta) == str(correcto):
            print("[+]")
        else:
            print("[-] -> " + correcto)

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

print("¿Que te apetece estudiar hoy?")
contador = 1
for i in vocabulariosTipo:
    print("\t[" + str(contador) + "]" + i)
    contador += 1

tema = input()
aptis = Vocabulary("alimentos.txt")
aptis.cargarVocabulario()
aptis.run()
