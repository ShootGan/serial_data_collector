import serial.tools.list_ports


class SerialSettings():
    """class contain parameters for serial port"""
    def __init__(self):
        self.bit_rate = (1200, 2400, 4800, 9600, 115200)
        self.ports = self._get_ports()
        self.current_bitrate = 9600
        self.current_port = None

    @staticmethod
    def _get_ports():
        """Returns all avilable ports and put them to dictionary whee {<port name>:<port description>}"""
        ports = serial.tools.list_ports.comports()
        return {port: descritpion for (port, descritpion, hwid) in ports}

    def update_bitrate(self, value: int) -> None:
        """Set chosen bit rate value"""
        if value > 256000:
            raise Exception("Baut rate is to big ")

        self.current_bitrate = value

    def update_port(self, port:str)-> None:
        if port in list(self.ports):
            self.current_port = port
        else:
            raise Exception("port doesn't exist")

