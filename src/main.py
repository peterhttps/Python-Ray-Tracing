import numpy as np
import matplotlib.pyplot as plt
from vector import *
from geometries import *
import math


# Image
aspectRatio = 16 / 9
width = 800
height = math.trunc(width / aspectRatio)
image = np.zeros((height, width, 3))

# Camera
viewportHeight = 2
viewportWidth = viewportHeight * aspectRatio
horizontal = vec3(viewportWidth, 0.0, 0.0)
vertical = vec3(0.0, viewportHeight, 0.0)
focalLenght = 1.0
origin = vec3(0.0 ,0.0, 0.0)
lowerLeftCorner = origin - (horizontal / 2) - (vertical / 2) - vec3(0.0, 0.0, focalLenght)

print("Imagem size %d x %d" % (width, height))

def backgroundColor(dir):
  t = 0.5 * (dir[1] + 1.0)
  return (1.0 - t) *  np.array([0.7, 0.8, 0.9]) + t*np.array([0.05, 0.05, 0.2])

def raycolor(ray, scenelist):
  record = HitRecord()

  # hitSphere(sphere, ray, 0.0, np.Infinity, record)

  orgn = np.array(ray.origin)
  dir = np.array(ray.direction)
  while (sceneListhit(scenelist, Ray(orgn, dir), 0.0001, np.Infinity, record)):
    dir = unitvector(reflect(dir, record.normal))
    orgn = record.p

  return backgroundColor(dir)

s1 = Sphere(vec3(0.0, 0.0, -1.0), 0.5)
s2 = Sphere(vec3(-1.0, 0.0, -2.0), 0.5)
s3 = Sphere(vec3(0.5, 1.5, -1.5), 0.5)
bigradius = 1000
floor = Sphere(vec3(0.0, -bigradius - 0.5, -1), bigradius)

world = SceneList()
world.push(s1)
world.push(s2)
world.push(s3)
world.push(floor)

for j in range(height):
  for i in range(width):      
    u = (i - 1) / (width - 1)
    v = 1.0 - (j - 1) / (height - 1)
    direc = lowerLeftCorner + u*horizontal + v*vertical - origin 
    ray = Ray(origin, direc)

    image[j, i] = np.clip(raycolor(ray, world), 0, 1)
  print(j, height)
plt.imsave('src/rendered/image8.png', image)