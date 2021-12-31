import numpy as np
import sys, time, random
from pygame_functions import *


numLetters = 5
numGuesses = 6

#Window size
windowWidth = 1200
windowHeight = 700
letterWidth = (windowWidth*0.9)/numLetters
letterHeight = (windowHeight*0.9)/(numLetters+1)

screenSize(windowWidth, windowHeight)

wordOptions = []


letters = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
size = 40
currentGuess = 0
labelExists = False

def pickWord():
    lines = open('5-letterWords.txt').read().splitlines()
    myline = random.choice(lines)
    print(myline)
    return myline

word = pickWord()


def checkLetters(mysteryWord):
    all_freq = {}

    for i in mysteryWord:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    return all_freq

def yellowLetter(temp_freq, letter):

    if ((letter in temp_freq) and (temp_freq[letter]!=0)):
        temp_freq[letter] -= 1
        return True
    else:
        return False



def displayGuesses(temp_freq):
    for i in range(len(letters[0])):
        for j in range(len(letters)):
            color = "red"
            if(yellowLetter(temp_freq, letters[j][i])):
                color = "yellow"
            if(letters[j][i] == word[i]):
                color = "green"
            label = makeLabel(letters[j][i], size, letterWidth*(i+1), letterHeight*(j+1), color)
            showLabel(label)

def makeGuess(currentGuess):
    guessBox = makeTextBox(int(windowWidth/2-windowWidth/8), int(windowHeight/100), int(windowWidth/2), 1, "Word Guess", numLetters , int(size))
    showTextBox(guessBox)
    guess = textBoxInput(guessBox)
    for i in range(len(letters[0])):
        letters[currentGuess][i] = guess[i]




while(currentGuess <numGuesses):
    temp_freq = checkLetters(word)
    displayGuesses(temp_freq)
    makeGuess(currentGuess)
    currentGuess += 1

displayGuesses(temp_freq)
endWait()