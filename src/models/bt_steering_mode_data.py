import json
from serialisable_base import SerialisableBase


class BtSteeringModeData(SerialisableBase):
    speedLeft = ""
    directionLeft = ""
    speedRight = ""
    directionRight = ""

    def __init__(self, json_def=None, json_file=None):
        super().__init__(json_def, json_file)

    def deserialise(self, json_dict):
        super().deserialise(json_dict)
