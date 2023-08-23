# fucntion to convert an Hexadecimal ASCII encoded into a message with the intended characters
# it returns a string of converted characters
def hexadecimalToAscii(isoString):

    # string to storage ascii text to be returned by function
    asciiString = ""

    for i in range(0, len(isoString), 2):

        # variable to storage a pair of characters to be analyzed
        pair = isoString[i: i + 2]

        # conversion from base 16 to unicode characters
        asciiChar = chr(int(pair, 16))

        # final alteration on variable to be returned
        asciiString = asciiString + asciiChar

    return asciiString

