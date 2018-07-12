"""
New architecture test
"""

import sys
import signal
import time

from utils import log
from miniboa import TelnetServer
from ecs_world import create_world, save_world, load_world
import telnet_server
import globals as GLOBALS
import constants

# Debugging
from debug import update_snapshot, log_objgraph

def signal_handler(signal, frame):
    """Make sure we close the db on shutdown"""
    log.info('SIGINT caught, shutting down...')
    #sync_db(force=True)
    sys.exit(0)


def main():

    # Get a global world context
    world, em = create_world()

    # test serialization
    '''
    save_world(world)
    world = None
    world = load_world()
    '''

    signal.signal(signal.SIGINT, signal_handler)

    #if __debug__:
    #    sys.settrace(tracer)

    # Start the clock
    #GLOBALS.EPOCH_S = int(time.strftime('%s', time.strptime(GLOBALS.GAME_EPOCH, '%Y/%m/%d %H:%M:%S')))
    #log.info('Converted GAME_EPOCH: %s -> %s', GLOBALS.GAME_EPOCH, GLOBALS.EPOCH_S)
    #log.info('Game time will be scaled by a factor of: %s', GLOBALS.TIME_FACTOR)
    #GLOBALS.boot_time = int(time.time())
    #GLOBALS.last_update = GLOBALS.boot_time

    #boot_userdb()
    #boot_db()

    log.info('Starting server on port %s', constants.PORT)

    server = TelnetServer(port=constants.PORT, timeout=.05)
    # set our own hooks for welcome/disconnect messaging
    server.on_connect = telnet_server.connect_hook
    server.on_disconnect = telnet_server.disconnect_hook

    #log.info('Starting event queue')
    #GLOBALS.Scheduler = EventQueue()
    ## Must be called BEFORE scheduling any events
    #update_game_time()
    #GLOBALS.Scheduler.add(delay=20, realtime=True, callback=log.debug, args=['--MARK--'], repeat=-1)
    #GLOBALS.Scheduler.add(delay=300, realtime=True, callback=update_snapshot, args=[], repeat=-1)
    ##GLOBALS.Scheduler.add(delay=600, realtime=True, callback=log_objgraph, args=[], repeat=-1)

    loop_count = 0
    while GLOBALS.GAME_RUNNING:
        # Tick / run game here
        loop_start = time.time()
        server.poll()
        telnet_server.kick_idlers()
#        process_commands()
#        send_prompts()
#        update_game_time()
#        GLOBALS.Scheduler.tick()
        loop_end = time.time()
        loop_count += 1
        if loop_count % 1000 == 0:
            log.debug('Loop time: %7.5f, total loops: %s', (loop_end - loop_start), loop_count)

    log.info('Server shutdown received')
#    sync_db(force=True)




if __name__ == '__main__':
    main()
