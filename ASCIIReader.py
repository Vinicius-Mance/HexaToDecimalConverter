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
    mit = ''
    bitMap = ''
    bitMapSize = 0
    while i < len(stringData):
        pair = ''
        pair = (pair + str(stringData[i]) + str(stringData[i + 1]))
        i = i + 2

        if re.search("[0-7]", stringData[8]):
            bitMapSize = 24
        else:
            bitMapSize = 40
        if i <= 8:
            mit = mit + pair
        elif i <= bitMapSize:
            bitMap = bitMap + pair
        else:
            arrayData.append(pair)

    # loop to separate hexadecimals in pairs
    #
    #   for (var i = 0; i < isoString.length; i += 2):
    #       decimalPairs.push(isoString[i] + isoString[i + 1])
    #   return decimalPairs;
    #

    # chr()
    # Prints the ASCII value of the input character
    # print(mit)
    print(bitMap)
    # print(arrayData)
    # return arrayData

print(ASCIIReader("./files/isorawdata","rawdata"))


