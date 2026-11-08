import numpy as np
import math

class Location:
    def __init__(self, *values):
        self.x = 0.0
        self.y = 0.0
        for i, v in enumerate(values):
            if hasattr(v, '__len__'):
                self.x = v[0]
                self.y = v[1]
                assert i == 0 and len(values) == 1, "Only one tuple !"
            else:
                if i == 0:
                    self.x = v
                else:
                    self.y = v

    def __str__(self):
        return f"({self.x:5.2f}, {self.y:5.2f})"

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError(f"Invalid index {index}, must be in [0, 1]")

    @staticmethod
    def to_location(loc):
        if isinstance(loc, Location):
            return loc
        else:
            return Location(loc)

    def __add__(self, other):
        o = Location.to_location(other)
        return Location(self.x + o.x, self.y + o.y)

    def __sub__(self, other):
        o = Location.to_location(other)
        return Location(self.x - o.x, self.y - o.y)

    def __radd__(self, other):
        o = Location.to_location(other)
        return Location(o.x + self.x, o.y + self.y)

    def __rsub__(self, other):
        o = Location.to_location(other)
        return Location(o.x - self.x, o.y - self.y)

    def __iadd__(self, other):
        o = Location.to_location(other)
        self.x += o.x
        self.y += o.y

    def __isub__(self, other):
        o = Location.to_location(other)
        self.x -= o.x
        self.y -= - o.y

    @property
    def length(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    @property
    def squared_length(self):
        return self.x*self.x + self.y*self.y

class Archi:

    def __init__(self, location):
        self.location = Location(location)

class WallPanel(Archi):
    pass

class VrtBearing:
    def __init__(self, height, width, depth):
        self.height = height
        self.width  = width
        self.depth  = depth

class HrzBearing:
    def __init__(self, width, height, depth):
        self.width  = width
        self.height = height
        self.depth  = depth

class LeftJamb(VrtBearing):
    pass

class RightJamb(VrtBearing):
    pass

class Pillar(VrtBearing):
    pass

class Lintel(HrzBearing):
    pass

class Sill(HrzBearing):
    pass

class Opening:

    def __init__(self, center, width, base, height):
        self.center = center
        self.width  = width
        self.base   = base
        self.height = height

        self.left_jamb = None
        self.right_jamp = None
        self.lintel = None
        self.sill = None

    @property
    def left(self):
        return self.center - self.width/2

    @property
    def right(self):
        return self.center + self.width/2

    @property
    def top(self):
        return self.base + self.height

    @property
    def corners(self):
        return [
            [self.left, self.base],
            [self.left, self.top],
            [self.right, self.top],
            [self.right, self.base]]

class Door(Opening):
    pass

class Window(Opening):
    pass

class Wall(Archi):

    def __init__(self, corner0, corner1, height, radius=0):
        self.corner0 = Location(corner0)
        self.corner1 = Location(corner1)
        self.height  = height
        self.radius  = radius

        self.openings = []

    @property
    def length(self):
        return (self.corner1 - self.corner0).length

    def add_opening(self, opening):
        self.openings.append(opening)

    def get_geometry(self, preview=False, lod=0.01):

        openings = sorted(self.openings, key=lambda o: o.left)

        locs = [[0.0, 0.0]]
        face = [0]
        for o in openings:
            corners = o.corners
            idx = len(locs)

            if o.base <= 0.001:
                locs.extend(corners)
                face.extend([idx, idx+1, idx+2, idx+3])
            else:
                locs.append([o.left, 0])
                locs.extend(corners)
                face.extend([idx, idx+1, idx+2, idx+3, idx+4, idx])

        idx = len(locs)
        locs.extend([[self.length, 0], [self.length, self.height], [0, self.height]])
        face.extend([idx, idx+1, idx+2])

        a = np.array(locs)

        print(a)
        print(face)


wall = Wall((0, 0), (10, 0), 2.4)
wall.add_opening(Door(6.0, .8, 0.0, 1.8))
wall.add_opening(Window(3.0, 1.1, 0.8, 1.0))


print(wall)
wall.get_geometry()
