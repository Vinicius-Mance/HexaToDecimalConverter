# main file for testing
# standard strings for testing

# (one bitmap):
# map1 = "7EFF4601A8E1E20A"

# (two bitmaps):
# map2 = "FEFF460128E1E20A0000000000000040"

# standard filepath for testing:
standardfile = './files/isorawdata'
from MessageStorage8583 import MessageStorage8583

for i in MessageStorage8583(standardfile):
    print(i)