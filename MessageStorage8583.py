from BitMapper import BitMapper
from ASCIIReader import ASCIIReader
from DBConfig import DBConfig
import mysql
import re

def MessageStorage8583(ISOString):

    asciiInfo = ASCIIReader(ISOString)
    # print("MTI: " + asciiInfo[0])
    # print("Bitmap: " + asciiInfo[1])
    print("Info: " + asciiInfo[2])
    # print(asciiInfo)

    # fields = BitMapper(asciiInfo[1])
    dbdata = DBConfig('./files/config.ini')

    connection = mysql.connector.connect(
        host=dbdata['host'],
        user=dbdata['user'],
        password=dbdata['password'],
        database=dbdata['database']
    )

    cursor = connection.cursor()
    query = f'SELECT element_log_iso, length_log_iso, description_log_iso FROM log_iso'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    fields = result
    tempStorage = []
    pointlessVar = ''

    for i in fields:
        print("Position: "+str(i[0])+" | Size: "+i[1]+" | Type: "+i[2])
        if re.search("LVAR", i[1]):
            pointlessVar = ''
            print("Position: " + str(i[0]) + " | Size: " + i[1] + " | Type: " + i[2])
            print("LVAR")
        elif re.search("ans", i[1]):
            pointlessVar = ''
            print("Position: " + str(i[0]) + " | Size: " + i[1] + " | Type: " + i[2])
            print("ans")
        elif re.search("an", i[1]):
            pointlessVar = ''
            print("Position: " + str(i[0]) + " | Size: " + i[1] + " | Type: " + i[2])
            print("an")
        elif re.search("as", i[1]):
            pointlessVar = ''
            print("Position: " + str(i[0]) + " | Size: " + i[1] + " | Type: " + i[2])
            print("as")
        elif re.search("ns", i[1]):
            pointlessVar = ''
            print("Position: " + str(i[0]) + " | Size: " + i[1] + " | Type: " + i[2])
            print("ns")
        elif re.search("a", i[1]):
            pointlessVar = ''
            print("Position: " + str(i[0]) + " | Size: " + i[1] + " | Type: " + i[2])
            print("a")
        elif re.search("n", i[1]):
            pointlessVar = ''
            print("Position: " + str(i[0]) + " | Size: " + i[1] + " | Type: " + i[2])
            print('n')
        elif re.search("s", i[1]):
            pointlessVar = ''
            print("Position: " + str(i[0]) + " | Size: " + i[1] + " | Type: " + i[2])
            print("s")
        elif re.search("b", i[1]):
            pointlessVar = ''
            print("Position: " + str(i[0]) + " | Size: " + i[1] + " | Type: " + i[2])
            print("b")
        else:
            pointlessVar = ''
            print("Position: " + str(i[0]) + " | Size: " + i[1] + " | Type: " + i[2])

    return tempStorage