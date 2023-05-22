# Python program to find the ASCII value of a character
from HexadecimalToBinary import HexadecimalToBinary
from HexadecimalToAscii import HexadecimalToAscii
import pandas as pd
import re
def ASCIIReader(data, type):

    # default location file for testing
    # "./files/isorawdata"

    # variable to store the data as a string to be interpreted

    if (type == "rawdata"):
        de = pd.read_csv(data)
        stringData = str(de.columns[0])
    elif (type == "string"):
        stringData = data
    else:
        return "Insert a valid data type"

    # variables to store data as strings to be returned at end of function
    i = 0
    mti = ''
    bitMap = ''
    messageData = ''

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
            mti = mti + HexadecimalToAscii(pair)

        # line to separate bitmap from rawdata
        elif i <= bitMapSize:
            bitMap = bitMap + HexadecimalToBinary(pair)
        else:
            messageData = messageData + HexadecimalToAscii(pair)

    finalMessage = [mti, bitMap, messageData]

    return finalMessage


