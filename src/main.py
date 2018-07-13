"""
New architecture test
"""

import sys
import signal

from utils import log
from world import World
from telnet_server import MyTelnetServer
from user.db import boot_userdb
from clock import start_clock, now
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
    world = World()

    # test serialization
    '''
    save_world(world)
    world = None
    world = load_world()
    '''

    signal.signal(signal.SIGINT, signal_handler)

    #if __debug__:
    #    sys.settrace(tracer)

    # Load user accounts
    boot_userdb()
    
    # Start the clock
    start_clock(constants.TIME_FACTOR)

    # Start the telnet server
    log.info('Starting server on port %s', constants.PORT)
    telnet = MyTelnetServer(entmgr, port=constants.PORT, 
                            banner=constants.WELCOME_BANNER)


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
        loop_start = now()
        # Process telnet server connections
        telnet.process()
#        send_prompts()
#        update_game_time()
#        GLOBALS.Scheduler.tick()
        world.update()
        loop_end = now()
        loop_count += 1
        if loop_count % 1000 == 0:
            log.debug('Loop time: %7.5f, total loops: %s', (loop_end - loop_start), loop_count)

    log.info('Server shutdown received')
#    sync_db(force=True)




if __name__ == '__main__':
    main()
