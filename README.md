PiGlow Spark
============

**PiGlow Spark** is a Python module for the [PiGlow][] addon by [Pimoroni][].

This was originally a fork of [Ben Lebherz][@benleb]'s [PyGlow][] which itself
is a fork of [Jason Barnett][@boeeerb_github]'s [PiGlow][Boeeerb_PiGlow].

Quick How To
------------
### Preparation of the system

These steps will allow your system to be aware of the PiGlow and to be able
communicate with it.

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

Also check that the driver modules are **not** blacklisted in the
```/etc/modprobe.d/raspi-blacklist.conf``` file. You can either delete or
comment (insert a ```#``` at the beginning of the line) these lines if they
exist:

```
# blacklist spi-bcm2708
# blacklist i2c-bcm2708
```

#### Reboot
Once you have completed the steps above, restart your Raspberry Pi.

```bash
$ sudo reboot
```

### Interactive mode
Enter interactive mode:
```bash
$ cd piglow_spark
$ sudo ./piglow_spark.py
```

Credits
-------

- Jason Barnett ([@Boeeerb][@boeeerb_github] on Github and
    [@boeeerb][@boeeerb_twitter] on Twitter) for his [PiGlow][Boeeerb_PiGlow]
    module.
- Ben Lebherz ([@benleb][] on Github and [@ben_leb][] on Twitter) for his
    [PyGlow][] module.
- Those who contributed to the aforementioned modules.

License
-------
[![CC_BY_NC_SA_IMG][]][CC_BY_NC_SA_LINK]

This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 3.0 Unported License. To view a copy of
this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a
letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View,
California, 94041, USA.

[PiGlow]: http://shop.pimoroni.com/products/piglow "Pimoroni's PiGlow"
[Pimoroni]: http://www.pimoroni.com/ "Pimoroni"
[PyGlow]: https://github.com/benleb/PyGlow "Ben Lebherz's PyGlow python module"
[@benleb]: https://github.com/benleb "Ben Lebherz on Github"
[@ben_leb]: https://twitter.com/ben_leb "Ben Lebherz on Twitter"
[@boeeerb_github]: https://github.com/Boeeerb "Jason Barnett on Github"
[@boeeerb_twitter]: https://twitter.com/boeeerb "Jason Barnett on Twitter"
[Boeeerb_PiGlow]: https://github.com/Boeeerb/PiGlow "Jason Barnett's PiGlow"
[CC_BY_NC_SA_LINK]: http://creativecommons.org/licenses/by-nc-sa/3.0/
[CC_BY_NC_SA_IMG]: https://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png
