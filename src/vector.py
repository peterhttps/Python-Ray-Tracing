import numpy as np
import math

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

def rayAt(ray, t):
  return ray.origin + t * ray.direction

def hitSphere(sphere, ray):
  # bhaskara
  a = normsquared(ray.direction)
  oc = ray.origin - sphere.center 
  halfb = dot(ray.direction, oc)
  c = normsquared(oc) - sphere.radius**2
  discriminant = (halfb*halfb) - a * c

  if (discriminant <= 0):
    return -1.0
  else: 
    return (-halfb - math.sqrt(discriminant)) / (a)

