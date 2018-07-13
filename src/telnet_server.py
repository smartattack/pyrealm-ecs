'''
Telnet Server code
'''

from utils import log
from miniboa import TelnetServer
import constants
from user.login import Login


# Timeouts
PLAYER_TIMEOUT = 1200
LOBBY_TIMEOUT = 180


class MyTelnetServer:
    def __init__(self, ecs, port, banner):
        '''Initialize TelnetServer'''
        self._banner = banner
        self._port = port
        self.clients = []
        self.lobby = {}
        self.players = {}
        self._server = TelnetServer(port=port, timeout=0.5)
        # set our own hooks for welcome/disconnect messaging
        self._server.on_connect = self._connect_hook
        self._server.on_disconnect = self._disconnect_hook


    def process_input(self):
        '''Handle connections and input'''
        self._poll()
        self._kick_idlers()
        self._process_commands()


    def process_output(self):
        '''Handle output to telnet clients'''
        pass


    def _connect_hook(self, client):
        """Initialization routine run when clients connect"""
        log.info('--> Received connection from %s, sending welcome banner', client.addrport())
        # Get terminal environment
        client.request_naws()
        client.request_terminal_type()
        #client.request_mccp()
        #client.request_msp()
        client.send_cc(constants.WELCOME_BANNER)
        self.clients.append(client)
        # Initial "user" is a login handler
        anonymous_user = Login(client)
        # Adding user to lobby activates it's driver() in main loop
        self.lobby[client] = anonymous_user


    def _disconnect_hook(self, client):
        """Overrides miniboa hook, gets called on client disconnection"""
        log.info("DISCONNECT_HOOK: Lost connection to %s", client.addrport())
        if client in self.lobby:
            log.info(' +-> Removing %s from lobby', client.addrport())
            del self.lobby[client]
        #if client in self.players:
        #    log.debug(' +-> Removing clients[%s]', self.players[client].player.name)
        #    save_object(self.players[client].player, logout=True)
        #    # FIXME: clean up player from instances/structures
        #    del self.players[client]
        log.debug(' +-> Removing self.clients[%s]', client.addrport())
        self.clients.remove(client)


    def _kick_idlers(self):
        """Scan for and deactivate clients which have surpassed idle timeout"""
        # We maintain separate timeouts for players vs lobby connections
        for client in self.clients:
            #if client in self.players:
            #    if client.idle() > PLAYER_TIMEOUT:
            #        do_quit(self.players[client].player, [])
            #        client.active = False
            #        log.info('Marking idle client inactive: %s', client.addrport())
            #elif client in self.lobby:
            if client in self.lobby:
                if client.idle() > LOBBY_TIMEOUT:
                    client.active = False
                    log.info('Marking idle client inactive: %s', client.addrport())
            else:
                log.error('Found client not in LOBBY or PLAYERS lists: %s', client.addrport())


    def _poll(self):
        '''Wraps TelnetServer.poll()'''
        self._server.poll()


    def _process_commands(self):
        """Handle user input"""
        for user in list(self.lobby.values()):
            # process commands
            if user.client.active and user.client.cmd_ready:
                user.driver()
        #for user in self.players.values():
        #    # process commands
        #    if user.client.active and user.client.cmd_ready:
        #        user.driver()
