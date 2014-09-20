#!/usr/bin/python
# Mediatek GPS setup script

from serial import Serial

dev = '/dev/ttyAMA0'
s = Serial(dev, 9600)
for _ in range(10):
   s.write('$PMTK251,115200*1F\r\n') # new baud rate
s.flush()
s.close()

s = Serial(dev, 115200)
for _ in range(10):
   s.write('$PMTK313,1*2E\r\n') # search SBAS satellite
for _ in range(10):
   s.write('$PMTK220,100*2F\r\n') # 10Hz update rate
for _ in range(10):
   s.write('$PMTK301,1*2D\r\n') # select WAAS
for _ in range(10):
   s.write('$PMTK313,1*2E\r\n') # enable SBAS
s.flush()
s.close()

