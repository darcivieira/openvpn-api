from telnetlib import Telnet


class Connector:
    def __init__(self, host: str = None, port: int = None):
        if not host or not port:
            raise ValueError('You must set all parameters needed')

        self._host = host
        self._port = port

    def connect(self):
        return Telnet(self._host, self._port)

    @staticmethod
    def command(connection, action):
        try:
            connection.write(bytes('\n', encoding='ascii'))
            connection.read_until(b'\n', 1)
            connection.write(bytes(f'{action}\n', encoding='ascii'))
            return connection.read_until(b'END\n', 1).decode('ascii')
        except Exception as e:
            print(f'We found an error: {e}')
