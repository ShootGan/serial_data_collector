import sys
import glob
import serial
import pytest
from src.Core.serial_setttings import SerialSettings


class TestSerialSettings:
    """Testing class for seriall setting"""

    def test_detect_com_ports(self):
        """compare cmd or bash serial port list with serial port list from _get_ports method"""
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        system_ports = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                system_ports.append(port)
            except (OSError, serial.SerialException):
                pass
        test_port_setting = SerialSettings()
        get_ports_list = [x for x in test_port_setting.ports.keys()]
        assert get_ports_list == system_ports






