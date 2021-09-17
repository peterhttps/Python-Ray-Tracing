import numpy as np
import matplotlib.pyplot as plt

width = 600
height = 800

image = np.zeros((width, height, 3))

for i in range(height):
  for j in range(width):
    r = (i - 1) / (height - 1)
    g = 1.0 - (j - 1) / (width - 1)
    b = 0.25

    image[j, i] = np.clip([r, g, b], 0, 1)

plt.imsave('rendered/image0.png', image)