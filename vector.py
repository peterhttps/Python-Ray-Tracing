import numpy as np
from numpy import linalg

def vec3(x, y, z):
  return np.array([x, y, z])

def normsquared(v):
  return np.linalg.norm(v)**2 

def norm(v):
  return np.linalg.norm(v)

def dot(v1, v2):
  return np.dot(v1, v2)

def unitvector(v):
  return v / norm(v)

class Ray:
  def __init__(self, origin, direction):
    self.origin = origin
    self.direction = unitvector(direction) 

class Sphere:
  def __init__(self, center, radius):
    self.center = center
    self.radius = radius


def hitSphere(sphere, ray):
  # bhaskara
  a = normsquared(ray.direction)
  oc = sphere.center - ray.origin
  b = 2.0 * dot(ray.direction, oc)
  c = normsquared(oc) - sphere.radius**2
  discriminant = (b*b) - 4 * a * c

  if (discriminant <= 0):
    return False
  else: 
    return True
