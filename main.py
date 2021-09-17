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

def raycolor(ray):
  t = 0.5 * (ray.direction[1] + 1.0)
  return (1.0 - t) *  np.array([1.0, 1.0, 1.0]) + t*np.array([0.5, 0.7, 1.0])

for j in range(height):
  for i in range(width):      
    u = (i - 1) / (width - 1)
    v = 1.0 - (j - 1) / (height - 1)
    direc = lowerLeftCorner + u*horizontal + v*vertical - origin 
    ray = Ray(origin, direc)

    image[j, i] = np.clip(raycolor(ray), 0, 1)

    # image[j, i] = np.clip([r, g, b], 0, 1)

plt.imsave('rendered/image0.png', image)