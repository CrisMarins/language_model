from nltk import bigrams, trigrams
from collections import defaultdict
import random

def testo(book):
    

    with open(book, "r", encoding="utf-8") as myfile:
         texto = myfile.read()

    texto=texto[:] 
    texto=texto.replace("."," . ")
    texto=texto.replace(","," , ")
    texto=texto.replace("?"," ? ")
    texto=texto.replace("¿"," ¿ ")
    texto=texto.replace("!"," ! ")
    texto=texto.replace("¡"," ¡ ")
    texto=texto.replace(";"," ; ")
    texto=texto.replace(":"," : ")

    texto2=texto.split()
    return texto2

def TriDictionary(textotot):
    modelTrigrams = defaultdict(lambda: defaultdict(lambda: 0))
    for w1, w2, w3 in trigrams(textotot, pad_right=True, pad_left=True):
        if log:
            print(w1, w2, w3)
        modelTrigrams[(w1, w2)][w3] += 1

    for w1_w2 in modelTrigrams:
        total_count = float(sum(modelTrigrams[w1_w2].values()))
        for w3 in modelTrigrams[w1_w2]:
            modelTrigrams[w1_w2][w3] /= total_count     

    return modelTrigrams
       


def BiDictionary(texto2):

    modelBigrams = defaultdict(lambda: defaultdict(lambda: 0))
    for w1, w2, in bigrams(texto2, pad_right=True, pad_left=True):
        if log:
            print(w1, w2)
        modelBigrams[w1][w2] += 1
    
    for w1 in modelBigrams:
        total_count = float(sum(modelBigrams[w1].values()))
        for w2 in modelBigrams[w1]:
            modelBigrams[w1][w2] /= total_count 
    
    return modelBigrams

def TriFrase(modelTrigrams, palabra1, palabra2, lunghezza):

    text = [palabra1, palabra2]

    errorNoAvailable = 0

    if dict(modelTrigrams[text[0], text[1]])=={}:
        print('error: secuencia no encontrada')
        errorNoAvailable = 1

    sentence_finished = False
    numberOfwords = 0
    maxNumberofWords = lunghezza


    
    while (not sentence_finished) and errorNoAvailable==0:
        r = random.random()
        
        if log:
            print('umbral random: ', r)
        accumulator = .0
        
        for word in modelTrigrams[tuple(text[-2:])].keys():
            accumulator += modelTrigrams[tuple(text[-2:])][word]
            
            if log:
                print('palabras anteriores -->', tuple(text[-2:]))
                print('palabra: ', word, ', probabilidad de palabra: ', modelTrigrams[tuple(text[-2:])][word],' --> probabilidad acumulada: ', accumulator)        
                        
        
            if accumulator >= r:
                numberOfwords+=1
                text.append(word)
                
                if log:
                    print('\tpalabra buena: ==>', word)
                    print('frase construida: ', ' '.join([t for t in text if t]))
                break
        if text[-2:] == [None, None]:
            sentence_finished = True
            
        if numberOfwords>=maxNumberofWords:
            sentence_finished = True
    
    if errorNoAvailable==0:
        print (' '.join([t for t in text if t]))

def BiFrase(modelBigrams, palabra1, lunghezza):

    text = [palabra1]

    errorNoAvailable = 0

    if dict(modelBigrams[text[0]])=={}:
        print('error: secuencia no encontrada')
        errorNoAvailable = 1

    sentence_finished = False
    numberOfwords = 0
    maxNumberofWords = lunghezza
    
    while (not sentence_finished) and errorNoAvailable==0:

        r = random.random()
        
        if log:
            print('umbral random: ', r)
        accumulator = .0
        
        for word in modelBigrams[text[-1]].keys():
            accumulator += modelBigrams[text[-1]][word]
            
            if log:
                print('palabras anteriores -->', text[-1])
                print('palabra: ', word, ', probabilidad de palabra: ', modelTrigrams[tuple(text[-2:])][word],' --> probabilidad acumulada: ', accumulator)        
                        
            if accumulator >= r:
                numberOfwords+=1
                text.append(word)
                
                if log:
                    print('\tpalabra buena: ==>', word)
                    print('frase construida: ', ' '.join([t for t in text if t]))
                break
        if text[-1] == [None]:
            sentence_finished = True
            
        if numberOfwords>=maxNumberofWords:
            sentence_finished = True
    
    if errorNoAvailable==0:
        print (' '.join([t for t in text if t]))
    