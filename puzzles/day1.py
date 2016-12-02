import re
import pdb

class GridNavigator(object):
    def __init__(self, directions_string):
        self.directions_string = directions_string
        self.x = 0
        self.y = 0
        self.direction = 'north'

    def parse_directions_string(self):
        directions = self.directions_string.split(' ')
        parsed_directions = [DirectionParser(x) for x in directions]

class DirectionParser(object):
    def __init__(self, direction_string):
        self.direction_string = direction_string
        self.parse_direction_string()

    def parse_direction_string(self):
        m = re.match(r'^(L|R)(\d+)$', self.direction_string)
        if not m:
            raise self.BadDirectionStringError("Unable to parse direction string")
        self.direction = m.group(1)
        self.distance = int(m.group(2))

    class BadDirectionStringError(Exception):
        pass
