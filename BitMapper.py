from HexadecimalToBinary import hexadecimalToBinary
import pandas as pd
import re


def BitMapper(ISOString):

    # array to access info from fields's data elements
    de = pd.read_excel(r'files\infotable.xls', index_col=0, sheet_name='ISO - todos')
    dataElements = []
    for i in de.index:
        dataElements.append(i)

    # array to access info from fields's length
    legt = pd.read_excel(r'files\infotable.xls', index_col=1, sheet_name='ISO - todos')
    length = []
    for i in legt.index:
        length.append(i)

    # array to access info from fields's description
    desc = pd.read_excel(r'files\infotable.xls', index_col=2, sheet_name='ISO - todos')
    description = []
    for i in desc.index:
        description.append(i)

    # getting binary code by calling hexadecimalToBinary external function
    binaryString = hexadecimalToBinary(ISOString)

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

print(BitMapper("7EFF4601A8E1E20A"))