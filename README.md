# NLP-Portfolio
Project Portfolio for CS 4395 Human Language Technologies
_________________________________________________________________________________________________________________________________________________________________________

## Overview of NLP
Document briefly detailing the history of NLP and my personal interest in it.


## Assignment 1: Text Processing with Python
[Link to .py](https://github.com/cmb170230/NLP-Portfolio/blob/85485e11ef077cc5f42e053b5996edab139d375e/Homework1_cmb170230.py)
This program takes in a .csv file of employee records, cleans up any formatting errors, and stores it on disk in a dictionary indexed by employee ID.
To run, simply call the python file with the path to the input data.csv file as a sysarg.

Sample Command: 
> python3 'C:\Users\benne\Google Drive\Laptop Sync\UTD\CS 4395\Assignments\Assignment 1\Homework1_cmb170230.py' 'C:\Users\benne\Google Drive\Laptop Sync\UTD\CS 4395\Assignments\Assignment 1\data\data.csv'

Some strengths I've found of python's text processing capabilities are the simplicity of using the re library as well as the convience of string slicing using indices inside the brackets. One thing I don't like however (although I understand this isn't related explicity to working with strings) is the lack of type declaration/static typing.
Before this assignment, I had never touched regular expressions before- while frustating at first, as I started to understand how to format them I thought back to a similar project I had done in C++ years ago and how much easier it would have been to use regular expressions, so I appreciate their power now. Additionally, the vast majority of python work I've done lately has been entirely focused around machine learning/data science applications, so this assignment was a nice review of more vanilla python coding.

## Assignment 2: Word Guessing Game and NLTK Basics
[Link to .py](https://github.com/cmb170230/NLP-Portfolio/blob/3653578734decc4993fb90fd01f95f24214a6861/WordGuess_cmb170230.py) This program takes in a large batch of text from a .txt file as a sysarg, tokenizes and preprocesses it, and extracts common nouns for use in a hangman-esque word guessing game.
Sample Command:
> python3 'C:\Users\benne\Google Drive\Laptop Sync\UTD\CS 4395\Assignments\Assignment 2\WordGuess_cmb170230.py' 'C:\Users\benne\Google Drive\Laptop Sync\UTD\CS 4395\Assignments\Assignment 2\anat19.txt'.

## Assignment 3: Exploration of WordNet
[Link to .ipynb](https://github.com/cmb170230/NLP-Portfolio/blob/045b16c1d0792120ac2190f8bcd981f6f91c3a5e/CS_4395_WordNet.ipynb)
This program/document is an exploration of the use of WordNet and basic related techniques to gain a preliminary understanding of a body of text and a critical analysis of the results. To run, simply open the file in Google Colab.

## Assignment 4: Language Guessing with N-grams
[Link to .py](https://github.com/cmb170230/NLP-Portfolio/blob/3cf5ab3749f09420ed7a8f9b3515176f63bf6835/N-grams/ngrams_1_cmb170230.py) 

This program takes in a large amount of text in three different languages as an input and processes them into dictionaries of counts for both unigrams and bigrams, ran separately due to the time required for construction. The second program, the language guessing component, takes the pickled dictionaries as input along with files containing test cases and correct answers. To run the first, enter the full file paths to the texts as sysargs. To run the second, make sure the pickled dictionaries are in the same directory as the program, then enter the test cases and solution paths as sysargs.
