
def ebcdicToAscii(isoString):

    asciiString = ''
    pair = ''

    for i in range(0, len(isoString), 2):
        # variable to storage a pair of characters to be analyzed
        pair = isoString[i: i + 2]

        if pair == '00':
            asciiString = asciiString + '00'
        elif pair == '01':
            asciiString = asciiString + '01'
        elif pair == '02':
            asciiString = asciiString + '02'
        elif pair == '03':
            asciiString = asciiString + '03'
        elif pair == '05':
            asciiString = asciiString + '09'
        elif pair == '07':
            asciiString = asciiString + '7F'
        elif pair == '0B':
            asciiString = asciiString + '0B'
        elif pair == '0C':
            asciiString = asciiString + '0C'
        elif pair == '0D':
            asciiString = asciiString + '0D'
        elif pair == '0E':
            asciiString = asciiString + '0E'
        elif pair == '0F':
            asciiString = asciiString + '0F'
        elif pair == '10':
            asciiString = asciiString + '10'
        elif pair == '11':
            asciiString = asciiString + '11'
        elif pair == '12':
            asciiString = asciiString + '12'
        elif pair == '13':
            asciiString = asciiString + '13'
        elif pair == '16':
            asciiString = asciiString + '08'
        elif pair == '18':
            asciiString = asciiString + '18'
        elif pair == '19':
            asciiString = asciiString + '19'
        elif pair == '1C':
            asciiString = asciiString + '1C'
        elif pair == '1D':
            asciiString = asciiString + '1D'
        elif pair == '1E':
            asciiString = asciiString + '1E'
        elif pair == '1F':
            asciiString = asciiString + '1F'
        elif pair == '25':
            asciiString = asciiString + '0A'
        elif pair == '26':
            asciiString = asciiString + '17'
        elif pair == '27':
            asciiString = asciiString + '1B'
        elif pair == '2D':
            asciiString = asciiString + '05'
        elif pair == '2E':
            asciiString = asciiString + '06'
        elif pair == '2F':
            asciiString = asciiString + '07'
        elif pair == '32':
            asciiString = asciiString + '16'
        elif pair == '37':
            asciiString = asciiString + '04'
        elif pair == '3C':
            asciiString = asciiString + '14'
        elif pair == '3D':
            asciiString = asciiString + '15'
        elif pair == '40':
            asciiString = asciiString + '20'
        elif pair == '4A':
            asciiString = asciiString + '5B'
        elif pair == '4B':
            asciiString = asciiString + '2E'
        elif pair == '4C':
            asciiString = asciiString + '3C'
        elif pair == '4D':
            asciiString = asciiString + '28'
        elif pair == '4E':
            asciiString = asciiString + '2B'
        elif pair == '4F':
            asciiString = asciiString + '21'
        elif pair == '50':
            asciiString = asciiString + '26'
        elif pair == '5A':
            asciiString = asciiString + '5D'
        elif pair == '5B':
            asciiString = asciiString + '24'
        elif pair == '5C':
            asciiString = asciiString + '2A'
        elif pair == '5D':
            asciiString = asciiString + '29'
        elif pair == '5E':
            asciiString = asciiString + '3B'
        elif pair == '5F':
            asciiString = asciiString + '5E'
        elif pair == '60':
            asciiString = asciiString + '2D'
        elif pair == '6A':
            asciiString = asciiString + '7C'
        elif pair == '6B':
            asciiString = asciiString + '2C'
        elif pair == '6C':
            asciiString = asciiString + '25'
        elif pair == '6D':
            asciiString = asciiString + '5F'
        elif pair == '6E':
            asciiString = asciiString + '3E'
        elif pair == '6F':
            asciiString = asciiString + '3F'
        elif pair == '79':
            asciiString = asciiString + '60'
        elif pair == '7A':
            asciiString = asciiString + '3A'
        elif pair == '7B':
            asciiString = asciiString + '23'
        elif pair == '7C':
            asciiString = asciiString + '40'
        elif pair == '7D':
            asciiString = asciiString + '27'
        elif pair == '7E':
            asciiString = asciiString + '3D'
        elif pair == '7F':
            asciiString = asciiString + '22'
        elif pair == '81':
            asciiString = asciiString + '61'
        elif pair == '82':
            asciiString = asciiString + '62'
        elif pair == '83':
            asciiString = asciiString + '63'
        elif pair == '84':
            asciiString = asciiString + '64'
        elif pair == '85':
            asciiString = asciiString + '65'
        elif pair == '86':
            asciiString = asciiString + '66'
        elif pair == '87':
            asciiString = asciiString + '67'
        elif pair == '88':
            asciiString = asciiString + '68'
        elif pair == '89':
            asciiString = asciiString + '69'
        elif pair == '91':
            asciiString = asciiString + '6A'
        elif pair == '92':
            asciiString = asciiString + '6B'
        elif pair == '93':
            asciiString = asciiString + '6C'
        elif pair == '94':
            asciiString = asciiString + '6D'
        elif pair == '95':
            asciiString = asciiString + '6E'
        elif pair == '96':
            asciiString = asciiString + '6F'
        elif pair == '97':
            asciiString = asciiString + '70'
        elif pair == '98':
            asciiString = asciiString + '71'
        elif pair == '99':
            asciiString = asciiString + '72'
        elif pair == 'A1':
            asciiString = asciiString + '7E'
        elif pair == 'A2':
            asciiString = asciiString + '73'
        elif pair == 'A3':
            asciiString = asciiString + '74'
        elif pair == 'A4':
            asciiString = asciiString + '75'
        elif pair == 'A5':
            asciiString = asciiString + '76'
        elif pair == 'A6':
            asciiString = asciiString + '77'
        elif pair == 'A7':
            asciiString = asciiString + '78'
        elif pair == 'A8':
            asciiString = asciiString + '79'
        elif pair == 'A9':
            asciiString = asciiString + '7A'
        elif pair == 'C0':
            asciiString = asciiString + '7B'
        elif pair == 'C1':
            asciiString = asciiString + '41'
        elif pair == 'C2':
            asciiString = asciiString + '42'
        elif pair == 'C3':
            asciiString = asciiString + '43'
        elif pair == 'C4':
            asciiString = asciiString + '44'
        elif pair == 'C5':
            asciiString = asciiString + '45'
        elif pair == 'C6':
            asciiString = asciiString + '46'
        elif pair == 'C7':
            asciiString = asciiString + '47'
        elif pair == 'C8':
            asciiString = asciiString + '48'
        elif pair == 'C9':
            asciiString = asciiString + '49'
        elif pair == 'D0':
            asciiString = asciiString + '7D'
        elif pair == 'D1':
            asciiString = asciiString + '4A'
        elif pair == 'D2':
            asciiString = asciiString + '4B'
        elif pair == 'D3':
            asciiString = asciiString + '4C'
        elif pair == 'D4':
            asciiString = asciiString + '4D'
        elif pair == 'D5':
            asciiString = asciiString + '4E'
        elif pair == 'D6':
            asciiString = asciiString + '4F'
        elif pair == 'D7':
            asciiString = asciiString + '50'
        elif pair == 'D8':
            asciiString = asciiString + '51'
        elif pair == 'D9':
            asciiString = asciiString + '52'
        elif pair == 'E0':
            asciiString = asciiString + '5C'
        elif pair == 'E2':
            asciiString = asciiString + '53'
        elif pair == 'E3':
            asciiString = asciiString + '54'
        elif pair == 'E4':
            asciiString = asciiString + '55'
        elif pair == 'E5':
            asciiString = asciiString + '56'
        elif pair == 'E6':
            asciiString = asciiString + '57'
        elif pair == 'E7':
            asciiString = asciiString + '58'
        elif pair == 'E8':
            asciiString = asciiString + '59'
        elif pair == 'E9':
            asciiString = asciiString + '5A'
        elif pair == 'F0':
            asciiString = asciiString + '30'
        elif pair == 'F1':
            asciiString = asciiString + '31'
        elif pair == 'F2':
            asciiString = asciiString + '32'
        elif pair == 'F3':
            asciiString = asciiString + '33'
        elif pair == 'F4':
            asciiString = asciiString + '34'
        elif pair == 'F5':
            asciiString = asciiString + '35'
        elif pair == 'F6':
            asciiString = asciiString + '36'
        elif pair == 'F7':
            asciiString = asciiString + '37'
        elif pair == 'F8':
            asciiString = asciiString + '38'
        elif pair == 'F9':
            asciiString = asciiString + '39'
        else:
            asciiString = asciiString + 'A1'
    return asciiString
