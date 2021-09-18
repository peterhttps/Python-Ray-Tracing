import numpy as np
import math
from geometries import *

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

def push(scenelist, object):
  scenelist.objects.append(object)

def hitSphere(sphere, ray, t_min, t_max, record):
  # bhaskara
  a = normsquared(ray.direction)
  oc = ray.origin - sphere.center 
  halfb = dot(ray.direction, oc)
  c = normsquared(oc) - sphere.radius**2
  discriminant = (halfb*halfb) - a * c

  if (discriminant <= 0):
    return False
  else: 
    sqrd = math.sqrt(discriminant)
    t = (-halfb - sqrd) / a
    if (t < t_min or t > t_max):
      t = (-halfb + sqrd) / a
      if (t < t_min or t > t_max):
        return False
      
    record.t = t
    record.p = rayAt(ray, t)
    outword_normal = unitvector(np.array(record.p - sphere.center))
    front_face = dot(ray.direction, outword_normal) < 0
    # print(front_face)
    # record.normal = front_face if outword_normal else -outword_normal
    if (front_face):
      record.normal = outword_normal
    else:
      record.normal = -outword_normal
    return True


def sceneListhit(sceneList, ray, t_min, t_max, record):
  hitAnything = False
  tempRecord = HitRecord()
  closestSoFar = t_max

  for object in sceneList.objects:
    if (hitSphere(object, ray, t_min, closestSoFar, tempRecord)):
      hitAnything = True
      closestSoFar = tempRecord.t

      record.p = tempRecord.p
      record.t = tempRecord.t
      record.normal = tempRecord.normal

  return hitAnything
