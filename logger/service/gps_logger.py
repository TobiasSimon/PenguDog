#!/usr/bin/env python
"""
  ___________________________________________________
 |  _____                       _____ _ _       _    |
 | |  __ \                     |  __ (_) |     | |   |
 | | |__) |__ _ __   __ _ _   _| |__) || | ___ | |_  |
 | |  ___/ _ \ '_ \ / _` | | | |  ___/ | |/ _ \| __| |
 | | |  |  __/ | | | (_| | |_| | |   | | | (_) | |_  |
 | |_|   \___|_| |_|\__, |\__,_|_|   |_|_|\___/ \__| |
 |                   __/ |                           |
 |  GNU/Linux based |___/  Multi-Rotor UAV Autopilot |
 |___________________________________________________|
  
 GPS Logger Service

 Copyright (C) 2014 Tobias Simon, Ilmenau University of Technology

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details. """


from os import sep
from scl import generate_map
from misc import daemonize, user_data_dir
from msgpack import loads
from datetime import datetime


def main(name):
   map = generate_map(name)
   gps_socket = map['gps']
   ts_socket = map['time_set']
   while not loads(ts_socket.recv()):
      pass
   now = datetime.today().isoformat().replace(':', '')
   prefix = user_data_dir + sep + 'log' + sep
   new_file = prefix + 'gps_' + now + '.log'
   f = open(new_file, "wb")
   while True:
      data = gps_socket.recv()
      f.write(data)
      f.flush()


daemonize('gps_logger', main)

