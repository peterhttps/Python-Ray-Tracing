import numpy as np

def vec3(x, y, z):
  return np.array([x, y, z])

def norm(v):
  return np.linalg.norm(v)

def unitvector(v):
  return v / norm(v)

class SceneList:
  def __init__(self):
    self.objects = []

  def push(self, object):
    self.objects.append(object)

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

