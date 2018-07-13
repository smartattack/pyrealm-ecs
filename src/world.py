from ecs import *
from collections import OrderedDict
from utils import log


class World:
    def __init__(self):
        self.entities = OrderedDict()
        self._systems = []
        self._dead_entities = set()


    def create_entity(self, name=None, uid=None):
        entity = Entity(name=name)
        log.debug("Created entity: %s(%s)", entity.name, entity.uid)
        self.entities[entity.uid] = entity


    def delete_entity(self, entity_id):
        """Mark entitiy for deletion"""
        self._dead_entities.add(entity_id)


    def name_exists(self, name):
        """Check whether there is already an entity with a given name"""
        for entity in self.entities.values():
            if entity.name == name:
                return True
        else:
            return False


    def _reap_dead_entities(self):
        """Garbage collect deleted entities"""
        if self._dead_entities:
            log.debug('Found dead entities, reaping:')
        for entity in self._dead_entities:
            log.debug(' * {} ({})', entity.uid, entity.name)
            for component in entity.components:
                log.debug('   -> Removing component: {}', component.name)
                del component
            del self.entities[entity.uid]
        self._dead_entities = set()


    def wipe(self):
        """Destroy the world!"""
        log.warning('World.wipe() called - RE-INITIALIZING World data!')
        self.__init__()


    def register_system(self, instance):
        """Add a system to the World, will be called by update
        Systems are called in the order in which they were added"""
        assert issubclass(instance.__class__, System)
        log.info('Registering system: %s', system.name)
        self._systems.append(instance)
        self._systems = sorted(self._systems, key=lambda a: a.priority, reverse=True)


    def unregister_system(self, instance):
        """Remove a system from the world.  Stops processing."""
        if instance in self._systems:
            log.info('Unregistering %s', system.name)
            self._systems.remove(instance)


    def update(self, *args, **kwargs):
        """Run processing on all systems, reap dead entities"""
        self._reap_dead_entities()
        log.debug('Running Systems:')
        for system in self._systems:
            log.debug(' * %s', system.name)
            system.update(*args, **kwargs)

