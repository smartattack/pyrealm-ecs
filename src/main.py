"""
New architecture test
"""

import sys

from utils import log
from ecs_world import create_world, save_world, load_world


def main():

    # Get a global world context
    world, em = create_world()

    # test serialization
    '''
    save_world(world)
    world = None
    world = load_world()
    '''

    # debugging
    '''
    print("\nAll entities:\n{}\n".format(world.all_entities()))
    print("\nAll components:\n{}\n".format(world._components))
    for entity in world.all_entities():
        print("Entity: {}  Components: {}".format(entity, world.components_for_entity(entity)))
    for entry in world.get_components(components.MetadataComponent, components.HealthComponent, components.StatsComponent):
        print("-----------[ Entity:{} ]-----------------".format(entry[0]))
        for comp in entry[1]:
            print('{}: {}'.format(comp.__class__.__name__, comp.__dict__))
    '''

if __name__ == '__main__':
    main()
