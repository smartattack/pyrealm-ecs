"""
New architecture test
"""

import logging
import sys
import esper
import components
import dill
from random import randint


class EntityType(object):
    """Defines a list of components to apply to an Entity()"""
    def __init__(self, name, component_list = None):
         self.name = name
         self.components = component_list


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
        print("Creating an entity of type: {}".format(entity_type.name))
        # All entities get a PropertyComponent
        metadata = components.MetadataComponent(entity_type = entity_type.name)
        entity = self.world.create_entity(metadata)
        for component_name in entity_type.components:
            print(" +-> Adding component {}".format(component_name))
            if component_name == 'HealthComponent':
                component = randomHealth()
            elif component_name == 'StatsComponent':
                component = randomStats()
            else:
                component = make_component(component_name)
            if component:
                print("     * Component found: {}".format(component))
                self.world.add_component(entity, component)
            else:
                print("     * Component not found, omitting")
        return entity

def randomHealth():
    """Initialize and return HealthComponent with random values"""
    return components.HealthComponent(maxhp=randint(10,100), hp=randint(10,100))

def randomStats():
    return components.StatsComponent(level=randint(1,100), money=randint(0,5000), xp=randint(0,1000), armor=randint(0,300))

    
def create_world():
    et_player = EntityType('player', ['InfoComponent', 'HealthComponent', 'LocationComponent', 'AttributeComponent', 'StatsComponent'])
    et_npc = EntityType('npc', ['InfoComponent', 'HealthComponent', 'LocationComponent', 'AttributeComponent', 'StatsComponent'])
    et_item = EntityType('item', ['InfoComponent', 'LocationComponent'])

    world = esper.World()
    em = EntityManager(world)
    try:
        for kind in [ et_player, et_npc, et_item, et_item, et_player ]:
            entity = em.create(kind)
#            randomize_settings(world, entity)
    except Exception as err:
        print("Actual exception: {}".format(err))
        raise AttributeError
    return (world, em)

def save_world(world):
    """Attempt to persist world to disk"""
    import dill
    try:
        dill.dump(world, open('world.save', 'wb'))
    except BaseException as err:
        print("Save failed: {}", err)

def load_world():
    """Attempt to load a world from disk"""
    try:
        return dill.load(open('world.save', 'rb'))
    except exception as err:
        print("Exception loading data: {}".format(err))        


def main():

    log = logging.Logger('bob')

    world, em = create_world()
    save_world(world)

    world = None

    world = load_world()

    print("\nAll entities:\n{}\n".format(world.all_entities()))
    print("\nAll components:\n{}\n".format(world._components))

    for entity in world.all_entities():
        print("Entity: {}  Components: {}".format(entity, world.components_for_entity(entity)))


    for entry in world.get_components(components.MetadataComponent, components.HealthComponent, components.StatsComponent):
        print("-----------[ Entity:{} ]-----------------".format(entry[0]))
        for comp in entry[1]:
            print('{}: {}'.format(comp.__class__.__name__, comp.__dict__))


    #print("\nEntities with NoneComponent:\n{}\n".format(world.entities_with_component('NoneComponent')))
    #print("\n\nWorld:\n{}\n".format(repr(world)))

if __name__ == '__main__':
    main()

