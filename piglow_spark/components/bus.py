#!/usr/bin/env python
"""Bus module."""
import RPi.GPIO as rpi
from smbus import SMBus

class Bus(object):
    """Control the Bus."""

    __I2C_ADDR = 0x54
    __EN_OUTPUT_ADDR = 0x00
    __EN_ARM1_ADDR = 0x13
    __EN_ARM2_ADDR = 0x14
    __EN_ARM3_ADDR = 0x15
    __UPD_PWM_ADDR = 0x16

    def __init__(self):
        if rpi.RPI_REVISION == 1:
            i2c_bus = 0
        elif rpi.RPI_REVISION == 2:
            i2c_bus = 1
        else:
            print("Unable to determine Raspberry Pi Hardware-Revision.")
            sys.exit(1)

        # Enables the LEDs
        self.__bus = SMBus(i2c_bus)

        # Enable the SN3218's output
        self.__bus.write_byte_data(Bus.__I2C_ADDR, Bus.__EN_OUTPUT_ADDR, 0x01)
        # Enable each led arm
        self.__bus.write_byte_data(Bus.__I2C_ADDR, Bus.__EN_ARM1_ADDR, 0xFF)
        self.__bus.write_byte_data(Bus.__I2C_ADDR, Bus.__EN_ARM2_ADDR, 0xFF)
        self.__bus.write_byte_data(Bus.__I2C_ADDR, Bus.__EN_ARM3_ADDR, 0xFF)

        self.__buffer = []
        self.__state = {0x07:0, 0x08:0, 0x09:0, 0x06:0, 0x05:0, 0x0A:0,
            0x12:0, 0x11:0, 0x10:0, 0x0E:0, 0x0C:0, 0x0B:0,
            0x01:0, 0x02:0, 0x03:0, 0x04:0, 0x0F:0, 0x0D:0}


    def set_led(self, led_address, brightness):
        """Set a LED's brightness."""
        self.__bus.write_byte_data(Bus.__I2C_ADDR, led_address, brightness)
        self.__state[led_address] = brightness

    def update(self):
        """Update the bus."""
        self.__bus.write_byte_data(Bus.__I2C_ADDR, Bus.__UPD_PWM_ADDR, 0xFF)

    def light_led(self, led_address, brightness):
        """Immediately light a LED."""
        self.set_led(led_address, brightness)
        self.update()

    def buffer(self, led_address, brightness):
        """Buffer a value for a LED."""
        self.__buffer.append((led_address, brightness))

    def empty_buffer(self):
        """Empty the bus's buffer."""
        self.__buffer = []

    def led_state(self, led_address):
        """Current brightness of a LED."""
        return self.__state[led_address]

    def dump(self):
        """Backup the current state and buffer of the bus."""
        return (self.__buffer[:], self.__state.copy())

    def restore(self, (bus_buffer, state)):
        """Restore previously dumped state and buffer."""
        for led_address in state:
            self.light_led(led_address, state[led_address])
        self.__buffer = bus_buffer[:]

    def flush(self):
        """Flush the buffer."""
        if self.__buffer:
            for led_address, brightness in self.__buffer:
                self.set_led(led_address, brightness)
            self.update()
            self.empty_buffer()

    def up_to_date(self):
        """Check whether there are LEDs waiting to be updated."""
        return self.__buffer == []
