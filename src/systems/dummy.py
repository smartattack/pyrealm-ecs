"""
Dummy System
for testing, not meant to be used in-game
"""

from ecs import System

class DummySystem(System):
    """This system will dump a list of entities, for testing purposes"""
    def __init__(self):
        """Initialize the system"""
        self.components = [ 'Health', 'Info' ]

    def update(self):
        """List entities"""
        for entity in self.entities:
            print("Entity: {}".format(entity))
