/*___________________________________________________
 |  _____                       _____ _ _       _    |
 | |  __ \                     |  __ (_) |     | |   |
 | | |__) |__ _ __   __ _ _   _| |__) || | ___ | |_  |
 | |  ___/ _ \ '_ \ / _` | | | |  ___/ | |/ _ \| __| |
 | | |  |  __/ | | | (_| | |_| | |   | | | (_) | |_  |
 | |_|   \___|_| |_|\__, |\__,_|_|   |_|_|\___/ \__| |
 |                   __/ |                           |
 |  GNU/Linux based |___/  Multi-Rotor UAV Autopilot |
 |___________________________________________________|
  
 SCL Logger Implementation

 Copyright (C) 2014 Tobias Simon, Ilmenau University of Technology

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details. */


#include <stdarg.h>
#include <stdio.h>
#include <malloc.h>
#include <zmq.h>
#include <syslog.h>
#include <msgpack.h>

#include <scl.h>
#include <threadsafe_types.h>
#include <opcd_interface.h>

#include "logger.h"
#include "util.h"


static void *log_socket = NULL;
msgpack_sbuffer sbuf;
msgpack_packer pk;
size_t name_len = 0;
const char *name = NULL;


int logger_open(const char *_name)
{
   ASSERT_ONCE();
   name = _name;
   name_len = strlen(name);
   msgpack_sbuffer_init(&sbuf);
   msgpack_packer_init(&pk, &sbuf, msgpack_sbuffer_write);
   log_socket = scl_get_socket("log_data");
   return (log_socket == NULL) ? -1 : 0;
}


void logger_write(char *file, loglevel_t level, unsigned int line, char *format, ...)
{
   ASSERT_NOT_NULL(log_socket);
   ASSERT_NOT_NULL(file);
   
   /* set-up buffer for varg-message: */
   char message_buffer[1024];
   va_list ap;
   va_start(ap, format);
   size_t msg_len = vsnprintf(message_buffer, sizeof(message_buffer), format, ap);
   va_end(ap);

   /* fill message: */
   msgpack_sbuffer_clear(&sbuf);
   msgpack_pack_array(&pk, 5); /* quintuple */
   msgpack_pack_raw(&pk, name_len);
   msgpack_pack_raw_body(&pk, name, name_len); /* 0: component name */
   msgpack_pack_int(&pk, level); /* 1: level */
   size_t file_len = strlen(file);
   msgpack_pack_raw(&pk, file_len);
   msgpack_pack_raw_body(&pk, file, file_len); /* 2: file */
   msgpack_pack_int(&pk, level); /* 3: line */
   msgpack_pack_raw(&pk, msg_len);
   msgpack_pack_raw_body(&pk, message_buffer, msg_len); /* 4: message */

   scl_copy_send_dynamic(log_socket, sbuf.data, sbuf.size);
}

