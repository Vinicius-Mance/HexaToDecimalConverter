from HexadecimalToBinary import hexadecimalToBinary
import pandas as pd
import re

def BitMapper(ISOString):


    de = pd.read_excel(r'files\infotable.xls', index_col=0, sheet_name='ISO - todos')
    dataElements = []

    legt = pd.read_excel(r'files\infotable.xls', index_col=1, sheet_name='ISO - todos')
    lenght = []

    desc = pd.read_excel(r'files\infotable.xls', index_col=2, sheet_name='ISO - todos')
    description = []

    binaryString = hexadecimalToBinary(ISOString)

    for i in de.index:
        dataElements.append(i)

    for i in legt.index:
        lenght.append(i)

    for i in desc.index:
        description.append(i)

    print(description)

BitMapper("7EFF4601A8E1E20A")