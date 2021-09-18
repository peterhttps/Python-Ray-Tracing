import numpy as np
import matplotlib.pyplot as plt
from vector import *
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
  return (1.0 - t) *  np.array([1.0, 1.0, 1.0]) + t*np.array([0.5, 0.7, 1.0])

def raycolor(ray, sphere):

  t = hitSphere(sphere, ray)

  if (t > 0.0):
    p = rayAt(ray, t)
    normal = unitvector(np.array(p - sphere.center))
    ncolor = 0.5 * (normal + 1) 
    return (np.array([ncolor[0], ncolor[1], ncolor[2]]))
  else: 
    return backgroundColor(ray.direction)

s1 = Sphere(vec3(0.0, 0.0, -1.0), 0.5)
for j in range(height):
  for i in range(width):      
    u = (i - 1) / (width - 1)
    v = 1.0 - (j - 1) / (height - 1)
    direc = lowerLeftCorner + u*horizontal + v*vertical - origin 
    ray = Ray(origin, direc)

    image[j, i] = np.clip(raycolor(ray, s1), 0, 1)

    # image[j, i] = np.clip([r, g, b], 0, 1)

plt.imsave('src/rendered/image3.png', image)