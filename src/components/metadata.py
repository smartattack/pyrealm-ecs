"""
Metadata Component
Defines extraneous component information
Entity creation date, type
"""

from ecs import Component

class Metadata(Component):
    """Metadata about Entity"""
    def __init__(self, entity_type=None):
        self._type = entity_type
        import time
        self._created = time.time()

    @property
    def entity_type(self):
        """Return entity type as string"""
        return self._type
    
    @entity_type.setter
    def entity_type(self, entity_type):
        """Set entity type to string"""
        self._type = entity_type

    @property
    def entity_created(self):
        """When was the entity created"""
        return self._created

