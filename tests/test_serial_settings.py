import sys
import glob
import serial
import pytest
import random
from src.Core.serial_setttings import SerialSettings


class TestSerialSettings:
    """Testing class for seriall setting"""

    def test_detect_com_ports(self):
        """compare cmd or bash serial port list with serial port list from _get_ports method"""
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        else:
            pytest.skip("skipping windows-only tests")

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

    def test_update_bitratet(self):
        """tests update bitrate to typical values """
        defult_value = 9600
        typical_bitrate_values = (1200, 2400, 4800, 9600, 115200)
        test_object = SerialSettings()
        assert test_object.current_bitrate == defult_value
        for birate in typical_bitrate_values:
            test_object.update_bitrate(birate)
            assert test_object.current_bitrate == birate

    def test_update_bitratet_too_big(self):
        """tests update bitrate to too big value"""
        value_bigger_than_limit = 256001
        test_object = SerialSettings()
        with pytest.raises(Exception):
            test_object.update_bitrate(value_bigger_than_limit)
        assert test_object.current_bitrate is not value_bigger_than_limit

    def test_update_port(self):
        """tests if current port can be correctly updated"""
        mock_ports_dict = {"com1": "desc1", "com2": "desc2", "com3": "desc1"}
        random_port = random.choice(list(mock_ports_dict))
        test_object = SerialSettings()
        test_object.ports = mock_ports_dict
        test_object.update_port(random_port)
        assert test_object.current_port == random_port
