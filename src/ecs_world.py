"""
New architecture test
"""
import sys
import dill
from random import randint

from utils import log
import esper
import components
import processors
import constants


entity_types = {
    'player': ['InfoComponent', 'HealthComponent', 'LocationComponent', 'AttributeComponent', 'StatsComponent'],
    'npc': ['InfoComponent', 'HealthComponent', 'LocationComponent', 'AttributeComponent', 'StatsComponent'],
    'item': ['InfoComponent', 'LocationComponent'],
}


def make_component(class_name: str, *args, **kwargs):
    """Return instance of component by name"""
    import components
    class_ = None
    try:
        class_ = getattr(components, class_name)(args, kwargs)
    except:
        pass
    return class_


class EntityManager(object):
    """Create and initialize Entities and Components"""
    def __init__(self, world):
        """Return an entity Manager object"""
        self.world = world

    def create(self, entity_type):
        """Returns an entity of the requested type"""
        log.info("Creating an entity of type: %s", entity_type)
        # All entities get a PropertyComponent
        metadata = components.MetadataComponent(entity_type = entity_type)
        entity = self.world.create_entity(metadata)
        for component_name in entity_types[entity_type]:
            log.info(" +-> Adding component %s", component_name)
            component = make_component(component_name)
            if component:
                #log.debug("     * Component found: %s", component)
                self.world.add_component(entity, component)
            else:
                #log.debug("     * Component not found, omitting")
                pass
        return entity

    
def create_world():

    world = esper.World()
    em = EntityManager(world)
    try:
        for kind in [ 'item', 'npc' ]:
            entity = em.create(kind)
    except Exception as err:
        print("Actual exception: {}".format(err))
        raise AttributeError
    return (world, em)

def save_world(world):
    """Attempt to persist world to disk"""
    import dill
    try:
        dill.dump(world, open(constants.WORLD_FILE, 'wb'))
    except BaseException as err:
        print("Save failed: {}", err)

def load_world():
    """Attempt to load a world from disk"""
    try:
        return dill.load(open(constants.WORLD_FILE, 'rb'))
    except exception as err:
        print("Exception loading data: {}".format(err))        


# Functions for generating fake/test content
def randomHealth():
    """Initialize and return HealthComponent with random values"""
    return components.HealthComponent(maxhp=randint(10,100), hp=randint(10,100))

def randomStats():
    return components.StatsComponent(level=randint(1,100), money=randint(0,5000), xp=randint(0,1000), armor=randint(0,300))
