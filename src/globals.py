"""
PyRealm - main server functionality lives here
outside of main.py so globals can be included more easily.
"""

# will be populated in main() with current time.time()
boot_time = -1

# List of client connections (TelnetClient)
clients = []

# users in lobby
lobby = {}

# logged in users
users = {}
players = {}

# Timeouts
PLAYER_TIMEOUT = 1200
LOBBY_TIMEOUT = 180

# default game state
GAME_RUNNING = True

# System resource snapshots
last_snapshot = None
current_snapshot = None

# Dawn of time for the game (YYYY/mm/dd HH:MM:SS)
GAME_EPOCH = '0776/07/04 12:00:00'
TIME_FACTOR = 24

# Scale factor for game time
TIME_FACTOR = 24

# Daylight changes
daylight_level = 0
daylight_message = [
    'The sky is now completely dark.  Only the stars and the moon light your way.',
    'The sky begins to brighten as the sun rises to the east.',
    'The sun is directly overhead.',
    'The sky dims as the sun begins to set.',
]

# Positions - these are parsed in the user command handler
# Move to globals?
Positions = ('dead', 'sleeping', 'sitting', 'fighting', 'standing')

