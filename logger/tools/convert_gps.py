
from os import getenv
from msgpack import Unpacker
from sys import stdin
unpacker = Unpacker(stdin)


# satellite info elements:
PRN = 0
USE = 1
ELV = 2
AZI = 3
SIG = 4

# gps data elements:
TIME =   0 # always
LAT =    1 # 2d fix ...
LON =    2
SATS =   3
SPEED =  4
COURSE = 5
HDOP =   6
ALT =    7 # 3d fix ...
VDOP =   8

def fix(gps):
   if len(gps) > 7:
      return 3
   elif len(gps) > 1:
      return 2
   else:
      return 0

def sprint(str, level):
   print ' ' * 3 * level + str

sprint('<?xml version="1.0" encoding="UTF-8" standalone="no"?>', 0)
sprint('<gpx version="1.1" creator="%s">' % getenv('USER'), 0)
sprint('<trk>', 1)
sprint('<trkseg>', 2)
for gps in unpacker:
   try:
      gps_fix = fix(gps)
      if gps_fix >= 2:
         sprint('<trkpt lat = "%f" lon = "%f">' % (gps[LAT], gps[LON]), 3)
         sprint('<hdop>%.1f</hdop>' % gps[HDOP], 4)
         sprint('<fix>%dd</fix>' % gps_fix, 4)
         sprint('<sat>%d</sat>' % gps[SATS], 4)
         sprint('<time>%s</time>' % gps[TIME], 4)
         if gps_fix == 3:
            sprint('<ele>%.1f</ele>' % gps[ALT], 4)
            sprint('<vdop>%.1f</vdop>' % gps[VDOP], 4)
         sprint('</trkpt>', 3)
   except:
      pass
sprint('</trkseg>', 2)
sprint('</trk>', 1)
sprint('</gpx>', 0)
