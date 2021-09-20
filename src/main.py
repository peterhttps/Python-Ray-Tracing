import numpy as np
import matplotlib.pyplot as plt
from vector import *
from geometries import *
import math
import random
from progress.bar import Bar

# Image
aspectRatio = 16 / 9
width = 800
height = math.trunc(width / aspectRatio)

# Camera
viewportHeight = 2
viewportWidth = viewportHeight * aspectRatio
horizontal = vec3(viewportWidth, 0.0, 0.0)
vertical = vec3(0.0, viewportHeight, 0.0)
focalLenght = 1.0
origin = vec3(0.0 ,0.0, 0.0)
lowerLeftCorner = origin - (horizontal / 2) - (vertical / 2) - vec3(0.0, 0.0, focalLenght)

print("Imagem size %d x %d" % (width, height))

def marscolor(dir):
  t = 0.5 * (dir[1] + 1.0)
  return (1.0 - t) *  np.array([0.7, 0.8, 0.9]) + t*np.array([0.05, 0.05, 0.2])

def backgroundColor(dir):
  t = 0.5 * (dir[1] + 1.0)
  return (1.0 - t) *  np.array([1.0, 1.0, 1.0]) + t*np.array([0.5, 0.7, 1.0])


def raycolor(ray, scenelist):
  record = HitRecord()

  # hitSphere(sphere, ray, 0.0, np.Infinity, record)

  if (sceneListhit(scenelist, ray, 0.0001, np.Infinity, record)):
    color = 0.5 * (record.normal + 1.0)
    return (color)

  # orgn = np.array(ray.origin)
  # dir = np.array(ray.direction)
  # while (sceneListhit(scenelist, Ray(orgn, dir), 0.0001, np.Infinity, record)):
  #   dir = unitvector(reflect(dir, record.normal))
  #   orgn = record.p

  return backgroundColor(ray.direction)
  # return marscolor(dir)

s1 = Sphere(vec3(0.0, 0.0, -1.0), 0.5)
# s2 = Sphere(vec3(-1.0, 0.0, -2.0), 0.5)
# s3 = Sphere(vec3(0.5, 1.5, -1.5), 0.5)
bigradius = 100.0
floor = Sphere(vec3(0.0, -bigradius - 0.5, -1), bigradius)

world = SceneList()
world.push(s1)
# world.push(s2)
# world.push(s3)
world.push(floor)

def render(samplesPerPixel=100):
  image = np.zeros((height, width, 3))
  bar = Bar('Rendering', max=height, suffix='%(percent)d%%')
  
  for j in range(height):
    for i in range(width):
      pixelColor = vec3(0.0, 0.0, 0.0)
      for n in range(samplesPerPixel):

        u = (i - 1 + random.random()) / (width - 1)
        v = 1.0 - (j - 1 + random.random()) / (height - 1)
        direc = lowerLeftCorner + u*horizontal + v*vertical - origin 
        ray = Ray(origin, direc)

        pixelColor += raycolor(ray, world) 

      image[j, i] = np.clip(pixelColor /samplesPerPixel, 0, 1)
    bar.next()    

  return image

frame = render()
plt.imsave('src/rendered/AAimage9.png', frame)