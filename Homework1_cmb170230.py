import sys
import pickle
import re

#Sample Command: python3 'C:\Users\benne\Google Drive\Laptop Sync\UTD\CS 4395\Assignments\Assignment 1\Homework1_cmb170230.py'
#'C:\Users\benne\Google Drive\Laptop Sync\UTD\CS 4395\Assignments\Assignment 1\data\data.csv'


def main():
    #retrieve file name from system arguments, read in data, and close the file
    fileName = sys.argv[1]
    with open(fileName, 'r') as inFile:
        rawRecords = inFile.readlines()
    #slice off first line and send to cleaning function
    rawRecords = rawRecords[1:]
    isAutomaticPhoneCorrection = input("Would you like phone numbers to be automatically corrected? [y/n]: ")
    isAutomaticPhoneCorrection = True if isAutomaticPhoneCorrection.lower() == 'y' else False
    cleanedRecords = cleanRawRecords(rawRecords, isAutomaticPhoneCorrection)

    #pickle records to file, then read back in
    pickle.dump(cleanedRecords, open("cleanData.p", "wb"))
    cleanPickle = pickle.load(open("cleanData.p", "rb"))

    #print records to the console
    print("Employee List: \n")
    for id in cleanPickle:
        cleanPickle[id].display()

def cleanRawRecords(raw, isAutoPhone) -> dict():
    cleanRecords = dict()
    for record in raw:
        #start by splitting string on the commas
        splitRecord = re.split(r',', record)

        #if the first and last names do not match Capital Case, correct them
        if not(re.match("[A-Z]{1}[a-z]*$", splitRecord[0])):
            splitRecord[0] = splitRecord[0][0].upper() + splitRecord[0][1:].lower()
        if not(re.match("[A-Z]{1}[a-z]*$", splitRecord[1])):
            splitRecord[1] = splitRecord[1][0].upper() + splitRecord[1][1:].lower()

        #handle middle initial presence and case sensitivity, additional case for if middle name or typos are present
        if not(re.match("[A-Za-z]{1}", splitRecord[2])):
            splitRecord[2] = "X"
        elif not(re.match("[A-Z]{1}", splitRecord[2])):
            splitRecord[2] = splitRecord[2].upper()
        elif re.match("[A-Za-z]{2,}", splitRecord[2]):
            splitRecord[2] = re.sub("[^A-Za-z]", "", splitRecord[2])
            splitRecord[2] = splitRecord[2][0].upper()

        #if the ID on record is not valid, prompt user until it is correct
        while not(re.match("^[A-Z]{2}[\d]{4}$", splitRecord[3])):
            print("ID is Invalid: " + splitRecord[3])
            splitRecord[3] = input("Please enter a Valid ID for " + splitRecord[1] + " " + splitRecord[0] + ", ex. [AB1234]: ")

        #correct phone number format by either prompting user or automatically removing non-digits and adding hyphens
        splitRecord[4] = re.sub("\n", "", splitRecord[4])
        while not(re.match("^[\d]{3}[-]{1}[\d]{3}[-]{1}[\d]{4}$", splitRecord[4])):
            print("Invalid Phone #: " + splitRecord[4])
            if isAutoPhone:
                splitRecord[4] = re.sub("\D", "", splitRecord[4])
                splitRecord[4] = splitRecord[4][0:3] + "-" + splitRecord[4][3:6] + "-" + splitRecord[4][6:]
                print("Automatic Correction: " + splitRecord[4])
            else:    
                splitRecord[4] = input("Please enter a Valid Phone # for " + splitRecord[1] + " " + splitRecord[0] + ", ex. [123-456-7890]: ")
        
        #add newly cleaned record to the dictionary
        cleanRecords.update({splitRecord[3]:Person(splitRecord[0], splitRecord[1], splitRecord[2], splitRecord[3], splitRecord[4])})
    print("\n")
    return cleanRecords

#the Person class stores records in a structured manner and allows easy formatted printing to console
class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone
    def display(self):
        print("Employee ID: " + self.id)
        print("\t" + self.first, self.mi, self.last)
        print("\t" + self.phone, "\n")

#check for proper file system argument input
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please enter a valid filename as a system argument.')
    else:
        main()   