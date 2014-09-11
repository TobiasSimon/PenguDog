#!/bin/bash
#  ___________________________________________________
# |  _____                       _____ _ _       _    |
# | |  __ \                     |  __ (_) |     | |   |
# | | |__) |__ _ __   __ _ _   _| |__) || | ___ | |_  |
# | |  ___/ _ \ '_ \ / _` | | | |  ___/ | |/ _ \| __| |
# | | |  |  __/ | | | (_| | |_| | |   | | | (_) | |_  |
# | |_|   \___|_| |_|\__, |\__,_|_|   |_|_|\___/ \__| |
# |                   __/ |                           |
# |  GNU/Linux based |___/  Multi-Rotor UAV Autopilot |
# |___________________________________________________|
#
# This Script install Binaries to /usr/local/bin
#
# Copyright (C) 2014 Tobias Simon, Ilmenau University of Technology
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


cd /usr/local/bin
sudo ln -f -s $PENGUDOG_PATH/blackbox/tools/filter_txt_col.py pd_filter_txt_col
sudo ln -f -s $PENGUDOG_PATH/blackbox/tools/msgpack_to_txt.py pd_msgpack_to_txt
sudo ln -f -s $PENGUDOG_PATH/blackbox/tools/compare_msgpack.py pd_compare_msgpack
sudo ln -f -s $PENGUDOG_PATH/opcd/tools/opcd_shell.sh pd_opcd_shell
sudo ln -f -s $PENGUDOG_PATH/autopilot/tools/replay.py pd_replay
sudo ln -f -s $PENGUDOG_PATH/autopilot/tools/shell/pilot_shell.sh pd_pilot_shell
sudo ln -f -s $PENGUDOG_PATH/scripts/clear_pidfiles.sh pd_clear_pidfiles
sudo ln -f -s $PENGUDOG_PATH/svctrl/svctrl.py pd_svctrl
sudo ln -f -s $PENGUDOG_PATH/icarus/tools/icarus_shell.sh pd_icarus_shell
sudo ln -f -s $PENGUDOG_PATH/autopilot/tools/calibration/cal_start.sh pd_cal_start
sudo ln -f -s $PENGUDOG_PATH/autopilot/tools/calibration/cal_finish.sh pd_cal_finish
sudo ln -f -s $PENGUDOG_PATH/autopilot/tools/omap3_pwm_test.py pd_omap3_pwm_test
sudo ln -f -s $PENGUDOG_PATH/scl/tools/scl_dump_msgpack.py pd_scl_dump_msgpack
sudo ln -f -s $PENGUDOG_PATH/scl/tools/scl_show_stats.py pd_scl_show_stats
sudo ln -f -s $PENGUDOG_PATH/rc_cal/tools/rc_cal.py pd_rc_cal
sudo ln -f -s $PENGUDOG_PATH/rc_cal/tools/rc_cal_dump.py pd_rc_cal_dump

