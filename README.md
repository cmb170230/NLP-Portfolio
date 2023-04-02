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
[Link to .py](https://github.com/cmb170230/NLP-Portfolio/blob/3653578734decc4993fb90fd01f95f24214a6861/WordGuess_cmb170230.py) 

This program takes in a large batch of text from a .txt file as a sysarg, tokenizes and preprocesses it, and extracts common nouns for use in a hangman-esque word guessing game.
Sample Command:
> python3 'C:\Users\benne\Google Drive\Laptop Sync\UTD\CS 4395\Assignments\Assignment 2\WordGuess_cmb170230.py' 'C:\Users\benne\Google Drive\Laptop Sync\UTD\CS 4395\Assignments\Assignment 2\anat19.txt'.

## Assignment 3: Exploration of WordNet
[Link to .ipynb](https://github.com/cmb170230/NLP-Portfolio/blob/045b16c1d0792120ac2190f8bcd981f6f91c3a5e/CS_4395_WordNet.ipynb)

This program/document is an exploration of the use of WordNet and basic related techniques to gain a preliminary understanding of a body of text and a critical analysis of the results. To run, simply open the file in Google Colab.

## Assignment 4: Language Guessing with N-grams
[Link to project folder](https://github.com/cmb170230/NLP-Portfolio/tree/main/N-grams) 

This program takes in a large amount of text in three different languages as an input and processes them into dictionaries of counts for both unigrams and bigrams, ran separately due to the time required for construction. The second program, the language guessing component, takes the pickled dictionaries as input along with files containing test cases and correct answers. To run the first, enter the full file paths to the texts as sysargs. To run the second, make sure the pickled dictionaries are in the same directory as the program, then enter the test cases and solution paths as sysargs.

## Assignment 5- Exploration of Various Sentence Parsing Techniques
[Link to .pdf](https://github.com/cmb170230/NLP-Portfolio/blob/7f1b0aa009f0347d1236955f76225b4f9c97e39d/Sentence_Parsing_cmb170230.pdf) 

This document outlines examples of PSG, Dependency, and SRL parsing of a particular sentence, manually writing the representations themselves and documenting what the various acronyms mean as well as analyzing the performance of each technique relative to each other.

## Assignment 6- Web Crawler and Knowledge Base Generator
[Link to project folder](https://github.com/cmb170230/NLP-Portfolio/tree/main/Web%20Crawler)

These programs scrape a specific cooking website and associated websites, then cleans the results and generates a knowledge base based on specific keywords. See the attached report for more details.

## Assignment 7- Text Classification using Basic ML Techniques
[Link to .ipynb](https://github.com/cmb170230/NLP-Portfolio/blob/67259e4424bf7bf3ec4d1170df7b67031bec6384/Text%20Classification/Sentiment%20Analysis%20with%20NB,%20LogRegression,%20and%20NN%20Classifiers.ipynb)

This notebook demonstrates sentiment analysis via a variety of basic machine learning techniques, incuding model performance metrics.
