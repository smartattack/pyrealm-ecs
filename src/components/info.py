"""
Info component
Nearly all objects will have this component
It is used by look/examine/describe
"""

from ecs import Component

class Info(Component):
    def __init__(self, description=None, short_desc=None):
        self.description = description
        self.short_desc = short_desc
        self.extra_desc = {}

    #FIXME: handle extra_desc setting and retrieval based on keyword matches
