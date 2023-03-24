import re

def hexadecimalToBinary(ISOString):

    # variable to be returned with the final binary code as a string
    binaryString = ''

    for i in ISOString:
        if i == "0":
            binaryString = binaryString + "0000"
        elif  i == "1":
            binaryString = binaryString + "0001"
        elif  i == "2":
            binaryString = binaryString + "0010"
        elif  i == "3":
            binaryString = binaryString + "0011"
        elif  i == "4":
            binaryString = binaryString + "0100"
        elif  i == "5":
            binaryString = binaryString + "0101"
        elif  i == "6":
            binaryString = binaryString + "0110"
        elif  i == "7":
            binaryString = binaryString + "0111"
        elif  i == "8":
            binaryString = binaryString + "1000"
        elif  i == "9":
            binaryString = binaryString + "1001"
        elif re.search("[a,A]",i):
            binaryString = binaryString + "1010"
        elif re.search("[b,B]",i):
            binaryString = binaryString + "1011"
        elif re.search("[c,C]", i):
            binaryString = binaryString + "1100"
        elif re.search("[d,D]", i):
            binaryString = binaryString + "1101"
        elif re.search("[e,E]", i):
            binaryString = binaryString + "1110"
        elif re.search("[f,F]", i):
            binaryString = binaryString + "1111"

    return binaryString

# print(hexadecimalToBinary("7EFF4601A8E1E20A"))