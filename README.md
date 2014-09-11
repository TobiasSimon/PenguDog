What is PenguDog?
===================

PenguDog is a branch of PenguPilot, which contains only the basic software infrastructure (without flight code)
for applications such as tracking antennas, logging devices, ...

Filesystem Contents
===================

Sensor Infrastructure:

- [gpsp](gpsp): gps publisher, similar to gpsd but much simpler; uses [NMEALib](https://github.com/AHR-Project/nmealib)
- [geomag](geomag): subscribes to gps position and date/time; publishes magnetic declination in degrees
- [elevmap](elevmap): subscribes to gps position; publishes SRTM3 elevation data

Supporting Infrastructures:

- [gpstime](gpstime): GPS time zone / date / time setting service
- [config](config): configuration files
- [scl](scl): signaling and communication link (IPC framework), see [config/system.yaml](config/system.yaml)
- [opcd](opcd): online parameter configuration daemon, see [config/params.yaml](config/params.yaml)
- [svctrl](svctrl): service management and control utility, see [config/services.yaml](config/services.yaml)
- [logger](logger): logging services and utility programs
- [shared](shared): shared libraries shared among all PenguDog components

Additional Features:

- [display](display): shows battery, mem, cpu, satellite status via I2C SSD1307 128x64 display from Adafruit
- [wifi_sensor](wifi_sensor): publishes wireless network data acquired via iwlist
- [wifi_loc](wifi_loc): combines gps measurements and wifi scan results and publishes it

Build System and Environment:

- [site_scons](site_scons): related to build system
- [SConstruct](SConstruct): scons build file
- [scripts](scripts): various scripts, e.g. bashrc

Software Dependencies:
- Gentoo: app-admin/sudo app-misc/screen dev-lang/python dev-lang/swig dev-libs/glib dev-libs/libyaml dev-libs/msgpack dev-libs/protobuf dev-libs/protobuf-c dev-python/imaging dev-python/msgpack dev-python/numpy dev-python/psutil dev-python/python-daemon dev-python/pyyaml dev-python/pyzmq dev-util/scons sys-power/cpufrequtils dev-python/pyproj sci-libs/gdal
- Ubuntu: realpath scons swig python-msgpack protobuf-compiler python-protobuf libmsgpack-dev libprotobuf-dev python-yaml protobuf-c-compiler libprotobuf-c0-dev libzmq-dev python-zmq libyaml-dev libglib2.0-dev python-daemon python-dev

