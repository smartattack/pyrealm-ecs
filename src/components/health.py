"""
Character Health
"""

from ecs import Component


class Health(Component):
    """Character Health component"""
    __slots__ = ('entity', 'Catalog', 'ComponentTypes', 'current', 'maxhp')
    defaults = dict([('current', 100), ('maxhp', 100)])

    def isdead(self):
        """Return true or false based on health"""
        if self._current <= 0:
            return True
        else:
            return False
