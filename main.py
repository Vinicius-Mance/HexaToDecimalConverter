# main file for testing
# standard string for testing
# (one bitmap): "7EFF4601A8E1E20A"
# (two bitmaps): "FEFF460128E1E20A0000000000000040"
# standard filepath for testing:
standardfile = './files/isorawdata'

from BitMapper import BitMapper
from HexadecimalToBinary import HexadecimalToBinary
from ASCIIReader import ASCIIReader

# print(ASCIIReader('./files/isorawdata')[1])
# print(ASCIIReader('./files/isorawdata')[2])
# print(BitMapper(ASCIIReader('./files/isorawdata')[1]))
print(ASCIIReader(standardfile))



