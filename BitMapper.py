from HexadecimalToBinary import HexadecimalToBinary
import pandas as pd
import re

def BitMapper(ISOString):

    sheetName = "ISO - todos"
    fileLocation = "files\infotable.xls"

    # array to access info from fields's data elements
    de = pd.read_excel(fileLocation, index_col=0, sheet_name=sheetName)
    dataElements = []
    for i in de.index:
        dataElements.append(i)

    # array to access info from fields's length
    legt = pd.read_excel(fileLocation, index_col=1, sheet_name=sheetName)
    length = []
    for i in legt.index:
        length.append(i)

    # array to access info from fields's description
    desc = pd.read_excel(fileLocation, index_col=2, sheet_name=sheetName)
    description = []
    for i in desc.index:
        description.append(i)

    # getting binary code by calling hexadecimalToBinary external function
    binaryString = HexadecimalToBinary(ISOString)

    # array to be filled and returned when calling BitMapper function
    bitMapInfo = []

    for index, i in enumerate(binaryString):

        # statement to save field if present
        if int(i) == 1:
            item = []
            item.append(dataElements[int(index)])
            item.append(length[int(index)])
            item.append(description[int(index)])
            bitMapInfo.append(item)

    return bitMapInfo
