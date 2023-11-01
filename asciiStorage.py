from bitMapper import bitMapper
from asciiReader import asciiReader
import re

# this function returns all the data, sorted and ready to be read
def asciiStorage(isoMessage):

    # variable to get all the fields present on the message by the ASCIIReader function
    asciiInfo = asciiReader(isoMessage)

    # variable to store binary bitmap from message
    isoString = asciiInfo[1]

    # variable to store data as a string
    messageData = asciiInfo[2]

    # variable to be returned at the end of function
    storage = []

    # message data position - variable to be used as a index on the loop ahead
    mdp = 0

    # this loop based on the present fields of the message, and the attributes the bitmap shows.
    # it searches for variable or fixed sized fields and sorts them out.
    # each individual While loop saves the sorted information, and progresses
    # the position that indicates where is the next information to be sorted in the
    # rawdata string by the mdp variable above
    for i in bitMapper(isoString):

        # condition to change the mdp position in case of a variable field
        if re.search("LLLVAR", i[1]):
            strSize = messageData[mdp] + "" + messageData[mdp + 1] + "" + messageData[mdp + 2]
            mdp = mdp + 3
        elif re.search("LLVAR", i[1]):
            strSize = messageData[mdp] + "" + messageData[mdp + 1]
            mdp = mdp + 2
        elif re.search("LVAR", i[1]):
            strSize = messageData[mdp]
            mdp = mdp + 1
        else:
            strSize = re.findall(r'\d+', i[1])[0]

        # sortableLoop - extra code found on UnusedCode file - code #0
        u = 0
        string = ''
        while u < int(strSize):
            string = string + messageData[mdp]
            mdp = mdp + 1
            u = u + 1
        array = dict()
        array["bit"] = str(i[0])
        array["length"] = i[1]
        array["description"] = i[2]
        array["value"] = string
        storage.append(array)

    return storage