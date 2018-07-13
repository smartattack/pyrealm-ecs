"""
Character Health
"""

from ecs import Component


class Health(Component):
    """Character Health component"""
    def __init__(self, current=10, maxhp=10):
        """Initialize with sane values"""
        self._current = current
        self._maxhp = maxhp
    
    @property
    def current(self):
        """Return current health"""
        return self._current
    
    @current.setter
    def current(self, value):
        """Set new health value"""
        self._current = value
        if self._current > self._maxhp:
            self._current = self._maxhp

    @property
    def maxhp(self):
        """Return max health"""
        return self._maxhp
    
    @maxhp.setter
    def maxhp(self, value):
        """Set new max health value"""
        self._maxhp = value

    def isdead(self):
        """Return true or false based on health"""
        if self._current <= 0:
            return True
        else:
            return False
