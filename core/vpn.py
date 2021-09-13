from openvpn.vpn import VPN


class OpenVPN:
    @staticmethod
    def __vpn():
        return VPN('localhost', 7505)

    def get_status(self):
        vpn = self.__vpn()
        connection = vpn.connect()
        data = vpn.get_status(connection)
        connection.close()
        return data

    def get_log(self):
        vpn = self.__vpn()
        connection = vpn.connect()
        data = vpn.get_log(connection)
        connection.close()
        return data

    def get_state(self):
        vpn = self.__vpn()
        connection = vpn.connect()
        data = vpn.get_state(connection)
        connection.close()
        return data