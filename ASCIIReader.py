# Python program to find the ASCII value of a character
from HexadecimalToBinary import HexadecimalToBinary
from HexadecimalToAscii import HexadecimalToAscii
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
    else:
        return "Insert a valid data type"

    i = 0
    mit = ''
    bitMap = ''
    messageData = ''

    while i < len(stringData):
        pair = ''
        pair = (pair + str(stringData[i]) + str(stringData[i + 1]))
        i = i + 2

        if re.search("[0-7]", stringData[8]):
            bitMapSize = 24
        else:
            bitMapSize = 40

        if i <= 8:
            mit = mit + HexadecimalToAscii(pair)
        elif i <= bitMapSize:
            bitMap = bitMap + HexadecimalToBinary(pair)
        else:
            messageData = messageData + HexadecimalToAscii(pair)

    finalMessage = [mit, bitMap, messageData]

    return finalMessage

print(ASCIIReader("./files/isorawdata","rawdata"))


