'''
Manage game time
'''

import time
from utils import log
import globals as GLOBALS


def start_clock(time_factor=24):
    '''Start game time, note time of boot'''
    GLOBALS.EPOCH_S = int(time.strftime('%s', time.strptime(GLOBALS.GAME_EPOCH, '%Y/%m/%d %H:%M:%S')))
    log.info('Converted GAME_EPOCH: %s -> %s', GLOBALS.GAME_EPOCH, GLOBALS.EPOCH_S)
    log.info('Game time will be scaled by a factor of: %s', time_factor)
    GLOBALS.boot_time = int(time.time())
    GLOBALS.last_update = GLOBALS.boot_time


def now():
    '''Return current realtime clock in seconds'''
    return time.time()
