from vector import *

class SceneObject:
  def __init__(self, objects):
    self.objects = objects

class HitRecord:
  def __init__ (self, p=vec3(0.0, 0.0, 0.0), t=0.0, normal=vec3(0.0, 0.0, 0.0)):
    self.p = p
    self.t = t
    self.normal = normal

class Ray:
  def __init__(self, origin, direction):
    self.origin = origin
    self.direction = unitvector(direction) 

class Sphere:
  def __init__(self, center, radius):
    self.center = center
    self.radius = radius

