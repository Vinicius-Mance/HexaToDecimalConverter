import re

def hexadecimalToDecimal(ISOString):

    decimalArray = []
    decimal = 0
    for i in ISOString:
        if re.search("[a,A]",i):
            decimalArray.append(10)
        elif re.search("[b,B]",i):
            decimalArray.append(11)
        elif re.search("[c,C]", i):
            decimalArray.append(12)
        elif re.search("[d,D]", i):
            decimalArray.append(13)
        elif re.search("[e,E]", i):
            decimalArray.append(14)
        elif re.search("[f,F]", i):
            decimalArray.append(15)
        else:
            decimalArray.append(int(i))

    counter = 15
    for i in decimalArray:
        decimal = decimal + i * pow(16,counter)
        counter = counter - 1

    return decimal



print(hexadecimalToDecimal("7EFF4601A8E1E20A"))