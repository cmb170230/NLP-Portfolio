import nltk
import sys
import re
import random

def main():
    #read in file input
    fileName = sys.argv[1]
    with open(fileName, 'r') as inFile:
        heartText = inFile.read()
    #send file input for preprocessing, retrieve list of noun counts, and construct 50 most common dict
    allTokens, nounTokens = tokenizeAndPreprocess(heartText)
    nounCounts = {tok:allTokens.count(tok) for tok in nounTokens}
    nounSorted = sorted(nounCounts.items(), key= lambda x: x[1], reverse=True)
    topNouns = [noun[0] for noun in nounSorted[:50]]

    #run the guessing game, prompt the user for continuous play
    userContinue = True
    while(userContinue):
        guessGame(topNouns)
        print("Would you like to play again? [y/n]:")
        userContinue = True if input() == 'y' else False
    

def guessGame(nouns):
    #initialize the game- set user score and select random word from noun list
    userScore = 5
    guessWord = [*nouns[random.randint(0,49)]]
    print("Let's Play a Word Guessing Game!!")
    guessDisplay = list()
    while len(guessDisplay) != len(guessWord):
        guessDisplay.append('_')
    while(userScore >= 0):
            #ensure proper formatting in terminal of current guess state
        print(' '.join(guessDisplay))
        print("Guess a Letter: ")
        userChar = input()
        #handle erronious input or the escape character
        if(len(userChar) > 1):
            print("Please only enter one letter.")
        elif(userChar == '!'):
            return
        else:
            #if the guess is found in the selected word, iterate through to catch all instances,
            #else prompt user to guess again and decrement score
            try:
                guessWord.index(userChar)
                print("Right!")
                for i in range(len(guessWord)):
                    if(userChar == guessWord[i]):
                        guessDisplay[i] = userChar
                userScore += 1
            except:
                print("Sorry, Guess Again")
                userScore -= 1
            print("Your current score is:", userScore)
            #if there are no more empty spaces in the display list, display the final score and exit
            try:
                guessDisplay.index('_')
            except:
                print("Congratulations! You Solved It!\nFinal Score: ", userScore)
                return


def tokenizeAndPreprocess(corpus):
    #tokenize input and calculate lexical diversity
    tokens = nltk.word_tokenize(corpus)
    lexDiv = len(set(tokens))/len(tokens)
    print("Lexical Diversity of the Text:", lexDiv, "\n")

    #remove words shorter than n = 5, make lowercase, and remove stopwords    
    tokens = [tok for tok in tokens if(len(tok) > 5 and tok.isalpha())]
    tokens = [tok.lower() for tok in tokens]
    from nltk.corpus import stopwords
    tokens = [tok for tok in tokens if(tok not in stopwords.words('english'))]

    #lemmatize, tag with POS, and print the first 20
    lem = nltk.WordNetLemmatizer()
    lemmaToken = [lem.lemmatize(tok) for tok in tokens]
    uniqueLemmaToken = list(set(lemmaToken))
    taggedULT = nltk.pos_tag(uniqueLemmaToken)
    print("First 20 Unique Lemmatized and Tagged Words: ")
    print(taggedULT[:20])

    #create list of only noun tokens, count all tokens, and return necessary output
        #iterate through POS tagged lemmatized tokens, if the tag begins with NN, add it to the noun list
    nounList = [tok[0] for tok in taggedULT if re.match("^[NN]{2,}", tok[1])]
    print("Number of tokens:", len(tokens), "\nNumber of nouns:", len(nounList), "\n")
    return tokens, nounList


#check for proper file system argument input
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a valid filename as a system argument.')
    else:
        main()   

