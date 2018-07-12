from enum import Enum

class WearComponent:
    """Wearable component data"""
    def __init__(self, slots=None):
        self._slots = set()
        if slots:
            self._slot.update(slot)

    @property
    def slots():
        return self._slot

class EquipmentSlots(Enum):
    MAIN_HAND = 1
    OFF_HAND = 2
