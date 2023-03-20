from HexadecimalToBinary import hexadecimalToBinary
import pandas as pd
import re

def BitMapper(ISOString):

    table = pd.read_excel(r'files\infotable.xls', index_col=0, sheet_name='ISO - todos')
    binaryString = hexadecimalToBinary(ISOString)

    dataElements = []

    for i in table.index:

        if ( bool(re.search("[A-Z,a-z.]",str(i))) == False and re.search("[0-9]", str(i))):
                print(str(i))





    # return table

    # return binaryString

print(BitMapper("7EFF4601A8E1E20A"))

# print(hexadecimalToBinary("7EFF4601A8E1E20A"))