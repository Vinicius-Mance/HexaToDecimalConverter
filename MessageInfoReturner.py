from MessageStorage8583 import MessageStorage8583
import os

def MessageInfoReturner(ISOString):

    data = MessageStorage8583(ISOString)
    filetext = []
    for i in data:
        line = f'Bit: {i["bit"]} - {i["description"]} - {i["value"]}'
        filetext.append(line)

    filepath = "./files/text file destination/"

    fileId = len(os.listdir(filepath))

    with open(f'{filepath}Message{fileId}.txt', 'w', encoding="utf-8") as f:
        for i in filetext:
            f.write(str(i))
            f.write('\n')