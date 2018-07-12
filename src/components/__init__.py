"""
ECS Components
"""

# FIXME: is there a way to get this to happen
# automagically?  It'd be great if we just loaded all
# the files in this module dir and imported them with the
# right namespacing

from components.metadata import MetadataComponent
from components.attribute import AttributeComponent
from components.health import HealthComponent
from components.info import InfoComponent
from components.location import LocationComponent
from components.wear import WearComponent
from components.stats import StatsComponent
