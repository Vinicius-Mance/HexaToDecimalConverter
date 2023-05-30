from BitMapper import BitMapper
from ASCIIReader import ASCIIReader
import re

def MessageStorage8583(ISOString):

    asciiInfo = ASCIIReader(ISOString)
    # print("MTI: " + asciiInfo[0])
    # print("Bitmap: " + asciiInfo[1])
    # print("Info: " + asciiInfo[2])
    # print(asciiInfo)

    isoString = asciiInfo[1]
    messageData = asciiInfo[2]

    print(BitMapper(isoString))
    print(messageData)
    tempStorage = []

    # message data position
    mdp = 0

    for i in BitMapper(isoString):

        # print("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2])
        # maxLogSize = re.findall(r'\d+', i[1])

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
            # print(strSize)

        if re.search("ans", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            tempStorage.append(array)


        elif re.search("an", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            tempStorage.append(array)

        elif re.search("as", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            tempStorage.append(array)

        elif re.search("ns", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            tempStorage.append(array)

        elif re.search("a", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            tempStorage.append(array)

        elif re.search("n", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            tempStorage.append(array)

        elif re.search("s", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            tempStorage.append(array)

        elif re.search("b", i[1]):
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            tempStorage.append(array)

        else:
            o = 0
            string = ''
            while o < int(strSize):
                string = string + messageData[mdp]
                mdp = mdp + 1
                o = o + 1
            array = []

            array.append("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2]+"| Info: "+ string)
            tempStorage.append(array)


    return tempStorage