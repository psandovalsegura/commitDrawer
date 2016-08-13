# Github Message Creator
#
# Draw a message through the "Contributions" visualization by scheduling when to commit
#
# Built 8/10/16 by Pedro Sandoval

import sys
import operator
import time
from datetime import date, timedelta

BLOCKS_HEIGHT = 7
BLOCKS_WIDTH = 52

def main():
     """
     The main method takes no parameters and is responsible for prompting 
     for a message and executing all the procedures to help user commit at
     the right times.
     """
     message = raw_input("Enter a message: ")

     #Check that the message is the correct length
     lengthOfMessage = len(message)
     while lengthOfMessage > 7 or lengthOfMessage <= 0:
          print("Please enter a valid message. The GitHub visual can only support a maximum of 7 characters.")
          message = raw_input("Enter a message: ")
          lengthOfMessage = len(message)


     commitArray = setUpArray(message)
     dates = assignCommitDates(commitArray)

     finalDay = dates[-1]
     print("The message will be ready on " +  str(finalDay.month) + "/" + str(finalDay.day) + "/" + str(finalDay.year) )
     printCharacters(commitArray)

     createdFilename = putDatesInFile(message, dates)
     elapsedDays = finalDay - date.today()
     print("Your GitHub Profile will look like this after " + str(elapsedDays.days) +  " days. \n" + "Please check " + createdFilename + " and commit on the assigned dates.")

def setUpArray(message): 
     """Creates an array of the characters in the message

     Parameters:
        message, a string of 7 characters MAX

     Returns:
        an array of 0 and 1's which draw out characters
     """
     commitArray = []
     for character in message:
          commitArray.extend(alphabet[character])
     
     commitArray = addExtraBlocks(commitArray, len(message))
     return commitArray

def addExtraBlocks(commitArray, lengthOfMessage):
     #Prepend 3 block columns to the front of the commit array, since after filling 7 characters, 3 columns remain
     preBlocks =     [0, 0, 0,
                      0, 0, 0, 
                      0, 0, 0, 
                      0, 0, 0, 
                      0, 0, 0,
                      0, 0, 0,
                      0, 0, 0]

     #Fill in empty characters at the beginning of the commit array
     additionalPreBlocks = [0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0] * (7 - lengthOfMessage)

     postBlocks = [0,
                   0,
                   0,
                   0,
                   0]

     commitArray = preBlocks + additionalPreBlocks + commitArray # + postBlocks will not be implemented for simplicity
     return commitArray

def printCharacters(commitArray): 
     """Displays the array of characters

     Parameters: 
          commitArray, an array of 0 and 1's
     """
     print("                                -------------------------------------                                ")

     for row in range(BLOCKS_HEIGHT):
          currentRowIndexes = range(row, BLOCKS_WIDTH * BLOCKS_HEIGHT, 7)
          for col in range(BLOCKS_WIDTH):
               print( "#" if commitArray[currentRowIndexes[col]] == 1 else "."),
          print;

def assignCommitDates(commitArray):
     """Creates an array of dates when the user should commit

     Parameters:
        commitArray, an array of 0 and 1's

     Returns:
        an array of date objects
     """
     dates = []
     commitBeginIndex = findFirstCommitDay(commitArray)

     today = date.today()

     for index in range(commitBeginIndex, len(commitArray)):
          if commitArray[index] == 1:
               dates.append(today)

          today = (today + timedelta(days = 1))

     return dates

def findFirstCommitDay(commitArray):
     """Finds the first day for commit

     Parameters:
        commitArray, an array of 0 and 1's

     Returns:
        an integer (index) of the column where committing should start
     """
     for index in range(len(commitArray)):
          if commitArray[index] == 1:
               return index

def putDatesInFile(message, datesArray):
     """Puts an array of dates into a file called commitDatesFor_<message>.txt

     Parameters:
        datesArray, an array of dates

     Returns:
        the name of the created file
     """
     filename = "commitDatesForMessage_" + message + ".txt"
     handle = open(filename, "wb")

     if datesArray[0] == date.today():
          handle.write("<---- Heads up, make sure to commit today! ----> \n")
     else: 
          handle.write("<---- Don't commit today! ----> \n")

     #Write the assigned days to commit to the file in checklist format
     for assignedDate in datesArray:
          handle.write("[ ] -- " + "Commit on " + str(assignedDate.month) + "/" + str(assignedDate.day) + "/" + str(assignedDate.year) + "\n")

     handle.close()

     return filename


# Arrays below represent character set that can be displayed on the git contributions visual

a = [0, 0, 0, 0, 0, 0, 0] + [0, 1, 1, 1, 1, 1, 1] + [1, 0, 0, 1, 0, 0, 0] + [1, 0, 0, 1, 0, 0, 0] + [1, 0, 0, 1, 0, 0, 0] + [0, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 0, 0, 0, 0]

b = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [1, 0, 0, 1, 0, 0, 1] + [1, 0, 0, 1, 0, 0, 1] + [1, 0, 0, 1, 0, 0, 1] + [0, 1, 1, 0, 0, 1, 1] + [0, 0, 0, 0, 0, 0, 0]

c = [0, 0, 0, 0, 0, 0, 0] + [0, 0, 1, 1, 1, 1, 0] + [0, 1, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 0]

d = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [1, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [0, 1, 0, 0, 0, 0, 1] + [0, 0, 1, 1, 1, 1, 0] + [0, 0, 0, 0, 0, 0, 0]

e = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [1, 0, 0, 1, 0, 0, 1] + [1, 0, 0, 1, 0, 0, 1] + [1, 0, 0, 1, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 0]

f = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [1, 0, 0, 1, 0, 0, 0] + [1, 0, 0, 1, 0, 0, 0] + [1, 0, 0, 1, 0, 0, 0] + [1, 0, 0, 0, 0, 0, 0] + [0, 0, 0, 0, 0, 0, 0]

g = [0, 0, 0, 0, 0, 0, 0] + [0, 1, 1, 1, 1, 1, 1] + [1, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 1, 0, 1] + [1, 0, 0, 0, 1, 0, 1] + [0, 1, 0, 0, 1, 1, 1] + [0, 0, 0, 0, 0, 0, 0]

h = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 1, 0, 0, 0] + [0, 0, 0, 1, 0, 0, 0] + [0, 0, 0, 1, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 0, 0, 0, 0]

i = [0, 0, 0, 0, 0, 0, 0] + [1, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [1, 1, 1, 1, 1, 1, 1] + [1, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 0]

j = [0, 0, 0, 0, 0, 0, 0] + [0, 0, 0, 0, 1, 1, 0] + [0, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [1, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 0, 0, 0, 0]

k = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 1, 1, 0, 0] + [0, 0, 1, 0, 1, 0, 0] + [0, 1, 0, 0, 0, 1, 0] + [1, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 0]

l = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 0]

m = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [0, 1, 0, 0, 0, 0, 0] + [0, 0, 1, 0, 0, 0, 0] + [0, 1, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 0, 0, 0, 0]

n = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [0, 0, 1, 0, 0, 0, 0] + [0, 0, 0, 1, 0, 0, 0] + [0, 0, 0, 0, 1, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 0, 0, 0, 0]
     
o = [0, 0, 0, 0, 0, 0, 0] + [0, 1, 1, 1, 1, 1, 0] + [1, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 0, 0, 1] + [0, 1, 1, 1, 1, 1, 0] + [0, 0, 0, 0, 0, 0, 0]

p = [0, 0, 0, 0, 0, 0, 0] + [0, 1, 1, 1, 1, 1, 1] + [1, 0, 0, 1, 0, 0, 0] + [1, 0, 0, 1, 0, 0, 0] + [1, 0, 0, 1, 0, 0, 0] + [0, 1, 1, 0, 0, 0, 0] + [0, 0, 0, 0, 0, 0, 0]

q = [0, 0, 0, 0, 0, 0, 0] + [0, 1, 1, 1, 1, 1, 0] + [1, 0, 0, 0, 0, 0, 1] + [1, 0, 0, 0, 1, 0, 1] + [1, 0, 0, 0, 0, 1, 0] + [0, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 0, 0, 0, 1]

r = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [1, 0, 0, 1, 0, 0, 0] + [1, 0, 0, 1, 1, 0, 0] + [1, 0, 0, 1, 0, 1, 0] + [0, 1, 1, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 0]

s = [0, 0, 0, 0, 0, 0, 0] + [0, 1, 1, 1, 0, 0, 1] + [1, 0, 0, 1, 0, 0, 1] + [1, 0, 0, 1, 0, 0, 1] + [1, 0, 0, 1, 0, 0, 1] + [1, 0, 0, 0, 1, 1, 0] + [0, 0, 0, 0, 0, 0, 0]

t = [0, 0, 0, 0, 0, 0, 0] + [1, 0, 0, 0, 0, 0, 0] + [1, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [1, 0, 0, 0, 0, 0, 0] + [1, 0, 0, 0, 0, 0, 0] + [0, 0, 0, 0, 0, 0, 0]

u = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 0] + [0, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 1] + [1, 1, 1, 1, 1, 1, 0] + [0, 0, 0, 0, 0, 0, 0]

v = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 0, 0] + [0, 0, 0, 0, 0, 1, 0] + [0, 0, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 1, 0] + [1, 1, 1, 1, 1, 0, 0] + [0, 0, 0, 0, 0, 0, 0]
     
w = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 0, 0, 1, 0] + [0, 0, 0, 0, 1, 0, 0] + [0, 0, 0, 0, 0, 1, 0] + [1, 1, 1, 1, 1, 1, 1] + [0, 0, 0, 0, 0, 0, 0]

x = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 0, 0, 0, 1, 1] + [0, 0, 1, 0, 1, 0, 0] + [0, 0, 0, 1, 0, 0, 0] + [0, 0, 1, 0, 1, 0, 0] + [1, 1, 0, 0, 0, 1, 1] + [0, 0, 0, 0, 0, 0, 0]

y = [0, 0, 0, 0, 0, 0, 0] + [1, 1, 1, 0, 0, 0, 0] + [0, 0, 0, 1, 0, 0, 0] + [0, 0, 0, 0, 1, 1, 1] + [0, 0, 0, 1, 0, 0, 0] + [1, 1, 1, 0, 0, 0, 0] + [0, 0, 0, 0, 0, 0, 0]

z = [0, 0, 0, 0, 0, 0, 0] + [1, 0, 0, 0, 0, 1, 1] + [1, 0, 0, 0, 1, 0, 1] + [1, 0, 0, 1, 0, 0, 1] + [1, 0, 1, 0, 0, 0, 1] + [1, 1, 0, 0, 0, 0, 1] + [0, 0, 0, 0, 0, 0, 0]

space = [0, 0, 0, 0, 0, 0, 0] + [0, 0, 0, 0, 0, 0, 0] + [0, 0, 0, 0, 0, 0, 0] + [0, 0, 0, 0, 0, 0, 0] + [0, 0, 0, 0, 0, 0, 0] + [0, 0, 0, 0, 0, 0, 0] + [0, 0, 0, 0, 0, 0, 0]

alphabet = {
     'a' : a,
     'b' : b,
     'c' : c,
     'd' : d,
     'e' : e,
     'f' : f,
     'g' : g,
     'h' : h,
     'i' : i,
     'j' : j,
     'k' : k,
     'l' : l,
     'm' : m,
     'n' : n,
     'o' : o,
     'p' : p,
     'q' : q,
     'r' : r,
     's' : s,
     't' : t,
     'u' : u,
     'v' : v,
     'w' : w,
     'x' : x,
     'y' : y,
     'z' : z,
     ' ' : space
 }

# The code below should run when loading the file:
if __name__ == "__main__":
    main()



