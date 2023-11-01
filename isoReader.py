# Python program to find the ASCII value of a character
from hexadecimalToBinary import hexadecimalToBinary
from hexadecimalToAscii import hexadecimalToAscii
import pandas as pd
import re

# this function gets an ascii message and interpret it, either by a rawdata filepath, or a string
# it returns an array with all the message information:
# Message Type Indicator, binary bitmap, and the information from the massage itself
def isoReader(data):

    # variable to store the data as a string to be interpreted
    try:
        de = pd.read_csv(data)
        stringData = str(de.columns[0])
    except:
        stringData = data

    # variables to store data as strings to be returned at end of function
    mti = ''
    bitMap = ''
    messageData = ''

    i = 0
    while i < len(stringData):

        # variable to manipulate raw data as pairs of hexadecimal values
        pair = ''
        pair = (pair + str(stringData[i]) + str(stringData[i + 1]))
        i = i + 2

        # line to identify presence of secondary bitmap
        if re.search("[0-7]", stringData[8]):
            bitMapSize = 24
        else:
            bitMapSize = 40

        # line to store Message Type Identifier (MTI)
        if i <= 8:
            mti = mti + hexadecimalToAscii(pair)

        # line to separate bitmap from rawdata
        elif i <= bitMapSize:
            bitMap = bitMap + hexadecimalToBinary(pair)
        else:
            messageData = messageData + hexadecimalToAscii(pair)

    finalMessage = [mti, bitMap, messageData]

    return finalMessage


