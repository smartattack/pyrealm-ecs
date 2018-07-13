"""
Location Component
Defines location within the world
"""

from ecs import Component

class Location(Component):
    def __init__(self, location=None):
        self.location = location
