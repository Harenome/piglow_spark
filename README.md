PyGlow
======

PyGlow is a small Python module for the PiGlow addon by Pimoroni, it will let you flex the LED muscles of this fantastic addon.
This is a fork of [Ben Lebherz](https://github.com/benleb "@ben_leb")'s [PyGlow](https://github.com/benleb/PyGlow) which is a fork of [Jason](https://github.com/Boeeerb "@Boeeerb")'s [PiGlow](https://github.com/Boeeerb/PiGlow).


Features
--------

 - Control a single LED, a single Arm, a single color or any combination of this
 - Gamma Correction, makes the progression from 0-255 more visually linear

Quick How To
------------
### Preparation of the system

These steps will allow your system to be aware of the PiGlow and to be able communicate with it.

#### Install the i2c libraries and python support
```bash
$ sudo apt-get install python-smbus
```

#### Enable the i2c driver modules
If not present, append these lines to the ```/etc/modules``` file:
```
i2c-dev
i2c-bcm2708
```

Also check that the driver modules are **not** blacklisted in the ```/etc/modprobe.d/raspi-blacklist.conf``` file. You can either delete or comment (insert a ```#``` at the beginning of the line) these lines if they exist:
```
# blacklist spi-bcm2708
# blacklist i2c-bcm2708
```

#### Reboot
Once you have completed the steps above, restart your Raspberry Pi.
```
sudo reboot
```

### Downloading of PyGlow
You can either execute the following command line directly on your Raspberry Pi, if git is available, or execute this on your personnal computer and then copy the files to your Raspberry Pi:
```bash
$ git clone https://github.com/HarnoRanaivo/PyGlow.git
```

Enter interactive mode:
```bash
$ cd PyGlow
$ sudo python pyglow.py
```
