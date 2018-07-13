"""
Player Stats component
"""

from ecs import Component
import constants

class Stats(Component):
    """Player stats"""
    def __init__(self, level=1, money=0, xp=0, armor=0):
        self._level = level
        self._money = money
        self._xp = xp
        self._armor = armor

    @property
    def level(self):
        """Return level"""
        return self._level

    @level.setter
    def level(self, level):
        """Set level"""
        self._level = level
        if self._level > constants.MAX_LEVEL:
            self._level = constants.MAX_LEVEL

    @property
    def xp(self):
        """Return character experience points"""
        return self._xp

    @xp.setter
    def xp(self, value):
        """Set new XP"""
        self._xp = value
        if self._xp < 0:
            self._xp = 0

    @property
    def armor(self):
        """Return character armor rating"""
        return self._armor

    @armor.setter
    def armor(self, value):
        """Set armor rating"""
        self._armor = value
        if self._armor < 0:
            self._armor = 0
        if self._armor > constants.MAX_ARMOR:
            self._armor = constants.MAX_ARMOR
