from BitMapper import BitMapper
from ASCIIReader import ASCIIReader
import re

# this function returns all the data, sorted and ready to be read
def MessageStorage8583(ISOString):

    # variable to get all the fields present on the message by the ASCIIReader function
    asciiInfo = ASCIIReader(ISOString)

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

    for i in BitMapper(isoString):

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

        # as of this moment, this sorter by type is redundant, however it might be useful in future implementations
        if re.search("ans", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            storage.append(array)


        elif re.search("an", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            storage.append(array)

        elif re.search("as", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            storage.append(array)

        elif re.search("ns", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            storage.append(array)

        elif re.search("a", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            storage.append(array)

        elif re.search("n", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            storage.append(array)

        elif re.search("s", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            storage.append(array)

        elif re.search("b", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            storage.append(array)

        else:
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            storage.append(array)

    return storage