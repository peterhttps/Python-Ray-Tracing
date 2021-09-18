from vector import *

class Ray:
  def __init__(self, origin, direction):
    self.origin = origin
    self.direction = unitvector(direction) 

class Sphere:
  def __init__(self, center, radius):
    self.center = center
    self.radius = radius

