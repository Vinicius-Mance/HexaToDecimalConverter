from asciiStorage import asciiStorage
import os

def asciiInfoReturner(ISOString):

    data = asciiStorage(ISOString)
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
    return f'decoded file Message{fileId}.txt located at {filepath}'