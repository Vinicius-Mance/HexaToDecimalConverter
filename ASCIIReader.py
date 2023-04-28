# Python program to find the ASCII value of a character
from HexadecimalToBinary import HexadecimalToBinary
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

    i = 0
    mitRough = []
    bitMapRough = ''
    messageDataRough = []
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
            mitRough.append(pair)
        elif i <= bitMapSize:
            bitMapRough = bitMapRough + pair
        else:
            messageDataRough.append(pair)

    print(mitRough)
    print(bitMapRough)
    print(messageDataRough)

    # mitRefined = ''
    #
    # for i in mitRough:
    #     refined = chr(int(i))
    #     mitRefined = mitRefined + refined
    #
    # bitMapRefined = HexadecimalToBinary(bitMapRough)
    #
    # messageDataRefined = ''
    # for i in messageDataRough:
    #     refined = chr(int(i))
    #     messageDataRefined = messageDataRefined + refined
    #
    # print(mitRefined)
    # print(bitMapRefined)
    # print(messageDataRefined)




    # return arrayData

print(ASCIIReader("./files/isorawdata","rawdata"))


