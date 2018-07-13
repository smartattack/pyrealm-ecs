"""
ECS Components
"""

# FIXME: is there a way to get this to happen
# automagically?  It'd be great if we just loaded all
# the files in this module dir and imported them with the
# right namespacing

from components.metadata import Metadata
from components.attributes import Attributes
from components.health import Health
from components.info import Info
from components.location import Location
from components.wear import Wear
from components.stats import Stats
