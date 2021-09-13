from openvpn.utils.connector import Connector
from openvpn.utils import organizer


class VPN(Connector):
    @organizer.organize_status
    def get_status(self, connection):
        return self.command(connection, 'status')

    @organizer.organize_log
    def get_log(self, connection):
        return self.command(connection, 'log all')

    @organizer.organize_state
    def get_state(self, connection):
        return self.command(connection, 'state')
