import serial.tools.list_ports


class SerialSettings():
    """class contain parameters for serial port"""

    def __init__(self):
        self.bit_rate = (1200, 2400, 4800, 9600, 115200)
        self.ports = self._get_ports()

    @staticmethod
    def _get_ports():
        """Returns all avilable ports and put them to dictionary whee {<port name>:<port description>}"""
        ports = serial.tools.list_ports.comports()
        return {port: descritpion for (port, descritpion, hwid) in ports}



