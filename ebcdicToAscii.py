
def ebcdicToAscii(isoString):

    if isoString == '00':
        return '00'
    elif isoString == '01':
        return '01'
    elif isoString == '02':
        return '02'
    elif isoString == '03':
        return '03'
    elif isoString == '05':
        return '09'
    elif isoString == '07':
        return '7F'
    elif isoString == '0B':
        return '0B'
    elif isoString == '0C':
        return '0C'
    elif isoString == '0D':
        return '0D'
    elif isoString == '0E':
        return '0E'
    elif isoString == '0F':
        return '0F'
    elif isoString == '10':
        return '10'
    elif isoString == '11':
        return '11'
    elif isoString == '12':
        return '12'
    elif isoString == '13':
        return '13'
    elif isoString == '16':
        return '08'
    elif isoString == '18':
        return '18'
    elif isoString == '19':
        return '19'
    elif isoString == '1C':
        return '1C'
    elif isoString == '1D':
        return '1D'
    elif isoString == '1E':
        return '1E'
    elif isoString == '1F':
        return '1F'
    elif isoString == '25':
        return '0A'
    elif isoString == '26':
        return '17'
    elif isoString == '27':
        return '1B'
    elif isoString == '2D':
        return '05'
    elif isoString == '2E':
        return '06'
    elif isoString == '2F':
        return '07'
    elif isoString == '32':
        return '16'
    elif isoString == '37':
        return '04'
    elif isoString == '3C':
        return '14'
    elif isoString == '3D':
        return '15'
    elif isoString == '40':
        return '20'
    elif isoString == '4A':
        return '5B'
    elif isoString == '4B':
        return '2E'
    elif isoString == '4C':
        return '3C'
    elif isoString == '4D':
        return '28'
    elif isoString == '4E':
        return '2B'
    elif isoString == '4F':
        return '21'
    elif isoString == '50':
        return '26'
    elif isoString == '5A':
        return '5D'
    elif isoString == '5B':
        return '24'
    elif isoString == '5C':
        return '2A'
    elif isoString == '5D':
        return '29'
    elif isoString == '5E':
        return '3B'
    elif isoString == '5F':
        return '5E'
    elif isoString == '60':
        return '2D'
    elif isoString == '6A':
        return '7C'
    elif isoString == '6B':
        return '2C'
    elif isoString == '6C':
        return '25'
    elif isoString == '6D':
        return '5F'
    elif isoString == '6E':
        return '3E'
    elif isoString == '6F':
        return '3F'
    elif isoString == '79':
        return '60'
    elif isoString == '7A':
        return '3A'
    elif isoString == '7B':
        return '23'
    elif isoString == '7C':
        return '40'
    elif isoString == '7D':
        return '27'
    elif isoString == '7E':
        return '3D'
    elif isoString == '7F':
        return '22'
    elif isoString == '81':
        return '61'
    elif isoString == '82':
        return '62'
    elif isoString == '83':
        return '63'
    elif isoString == '84':
        return '64'
    elif isoString == '85':
        return '65'
    elif isoString == '86':
        return '66'
    elif isoString == '87':
        return '67'
    elif isoString == '88':
        return '68'
    elif isoString == '89':
        return '69'
    elif isoString == '91':
        return '6A'
    elif isoString == '92':
        return '6B'
    elif isoString == '93':
        return '6C'
    elif isoString == '94':
        return '6D'
    elif isoString == '95':
        return '6E'
    elif isoString == '96':
        return '6F'
    elif isoString == '97':
        return '70'
    elif isoString == '98':
        return '71'
    elif isoString == '99':
        return '72'
    elif isoString == 'A1':
        return '7E'
    elif isoString == 'A2':
        return '73'
    elif isoString == 'A3':
        return '74'
    elif isoString == 'A4':
        return '75'
    elif isoString == 'A5':
        return '76'
    elif isoString == 'A6':
        return '77'
    elif isoString == 'A7':
        return '78'
    elif isoString == 'A8':
        return '79'
    elif isoString == 'A9':
        return '7A'
    elif isoString == 'C0':
        return '7B'
    elif isoString == 'C1':
        return '41'
    elif isoString == 'C2':
        return '42'
    elif isoString == 'C3':
        return '43'
    elif isoString == 'C4':
        return '44'
    elif isoString == 'C5':
        return '45'
    elif isoString == 'C6':
        return '46'
    elif isoString == 'C7':
        return '47'
    elif isoString == 'C8':
        return '48'
    elif isoString == 'C9':
        return '49'
    elif isoString == 'D0':
        return '7D'
    elif isoString == 'D1':
        return '4A'
    elif isoString == 'D2':
        return '4B'
    elif isoString == 'D3':
        return '4C'
    elif isoString == 'D4':
        return '4D'
    elif isoString == 'D5':
        return '4E'
    elif isoString == 'D6':
        return '4F'
    elif isoString == 'D7':
        return '50'
    elif isoString == 'D8':
        return '51'
    elif isoString == 'D9':
        return '52'
    elif isoString == 'E0':
        return '5C'
    elif isoString == 'E2':
        return '53'
    elif isoString == 'E3':
        return '54'
    elif isoString == 'E4':
        return '55'
    elif isoString == 'E5':
        return '56'
    elif isoString == 'E6':
        return '57'
    elif isoString == 'E7':
        return '58'
    elif isoString == 'E8':
        return '59'
    elif isoString == 'E9':
        return '5A'
    elif isoString == 'F0':
        return '30'
    elif isoString == 'F1':
        return '31'
    elif isoString == 'F2':
        return '32'
    elif isoString == 'F3':
        return '33'
    elif isoString == 'F4':
        return '34'
    elif isoString == 'F5':
        return '35'
    elif isoString == 'F6':
        return '36'
    elif isoString == 'F7':
        return '37'
    elif isoString == 'F8':
        return '38'
    elif isoString == 'F9':
        return '39'
    else:
        return 'A1'
