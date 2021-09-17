import numpy as np
from numpy import linalg

def vec3(x, y, z):
  return np.array([x, y, z])

def normsquared(v):
  return np.linalg.norm(v, ord=2) 

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

