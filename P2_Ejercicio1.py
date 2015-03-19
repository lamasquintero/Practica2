#Practica 2 de Sistemas Distribuídos
##Practica realizada por Jose Manuel Martinez Gonzalez y Gonzalo Lamas Quintero

# -*- coding: utf-8 -*-

#Funcion que abre el fichero pokemon.txt

def FicheroPokemon():
    f = open("pokemon.txt")
    lista = f.readlines()     #Obtiene el contenido del fichero
    f.close()
    palabras = []
    for i in lista:
        for j in i.split(" "):
            if(j != "\n"):
                palabras.append(j)
    return palabras

#Funcion que devuelve un booleano indicando si la 1º cadena
#termina por la misma letra que empieza la 2º cadena.

def ComparaP(cad1,cad2):
    if(cad1!=cad2):
        return cad1(-1)==cad2(0)
    else:
        return false

#principal
Palabras = FicheroPokemon()
NumPokemon = len(Palabras)
TamMax = 0      #Contador para obtener la cadena mas larga
Cadena = []
for i in NumPokemon:
    Cadena.append(Palabras[i])
    num = len(Cadena)
    j=0     #Modificamos el valor de este elemento para reiniciar el bucle
    for j in NumPokemon:      #Este bucle se reinicia al encontrar una palabra
        for k in Palabras:
            if(ComparaP(Palabras[i],k)):
                Cadena.append(Palabras[i])
                Palabras[i]=k
                j=0     #Reiniciamos el bucle
    
    TamCadena = len(Cadena)
    if(TamCadena>TamMax):
        TamMax=len(Cadena)
        CadenaFinal=Cadena
    
    Cadena = []     #Vaciamos la cadena para la siguiente iteracion 
    
print CadenaFinal
print "Su tamaño es ",TamMax
