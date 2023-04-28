# Python program to find the ASCII value of a character
import pandas as pd
import re

def ASCIIReader(data, type):

    # default location file for testing
    # "./files/isorawdata"

    # variable to store the data as a string to be interpreted
    stringData = ''

    if (type == "rawdata"):
        de = pd.read_csv(data)
        stringData = str(de.columns[0])
    elif (type == "string"):
        stringData = data
    else :
        return "Insert a valid data type"

    arrayData = []

    i = 0
    while i < len(stringData):
        pair = ''
        pair = (pair + str(stringData[i]) + str(stringData[i + 1]))
        i = i + 2
        arrayData.append(pair)
    # loop to separate hexadecimals in pairs
    #
    #   for (var i = 0; i < isoString.length; i += 2):
    #       decimalPairs.push(isoString[i] + isoString[i + 1])
    #   return decimalPairs;
    #

    # chr()
    # Prints the ASCII value of the input character

    return arrayData

print(ASCIIReader("./files/isorawdata","rawdata"))


