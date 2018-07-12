'''
Telnet Server code
'''

from utils import log
import constants
from user.login import Login
import globals as GLOBALS

def connect_hook(client):
    """Initialization routine run when clients connect"""
    log.info('--> Received connection from %s, sending welcome banner', client.addrport())
    # Get terminal environment
    client.request_naws()
    client.request_terminal_type()
    #client.request_mccp()
    #client.request_msp()
    client.send_cc(constants.WELCOME_BANNER)
    GLOBALS.clients.append(client)
    # Initial "user" is a login handler
    anonymous_user = Login(client)
    # Adding user to lobby activates it's driver() in main loop
    GLOBALS.lobby[client] = anonymous_user


def disconnect_hook(client):
    """Overrides miniboa hook, gets called on client disconnection"""
    log.info("DISCONNECT_HOOK: Lost connection to %s", client.addrport())
    if client in GLOBALS.lobby:
        log.info(' +-> Removing %s from lobby', client.addrport())
        del GLOBALS.lobby[client]
    if client in GLOBALS.players:
        log.debug(' +-> Removing clients[%s]', GLOBALS.players[client].player.name)
        save_object(GLOBALS.players[client].player, logout=True)
        # FIXME: clean up player from instances/structures
        del GLOBALS.players[client]
    log.debug(' +-> Removing GLOBALS.clients[%s]', client.addrport())
    GLOBALS.clients.remove(client)

def kick_idlers():
    """Scan for and deactivate clients which have surpassed idle timeout"""
    # We maintain separate timeouts for players vs lobby connections
    for client in GLOBALS.clients:
        if client in GLOBALS.players:
            if client.idle() > GLOBALS.PLAYER_TIMEOUT:
                do_quit(GLOBALS.players[client].player, [])
                client.active = False
                log.info('Marking idle client inactive: %s', client.addrport())
        elif client in GLOBALS.lobby:
            if client.idle() > GLOBALS.LOBBY_TIMEOUT:
                client.active = False
                log.info('Marking idle client inactive: %s', client.addrport())
        else:
            log.error('Found client not in LOBBY or PLAYERS lists: %s', client.addrport())
