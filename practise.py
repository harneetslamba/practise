class Polygon:
    def __init__(self, num_sides, *args, **kwargs):
        self.num_sides = num_sides
        print('the number of sides {}'.format(self.num_sides))
        print('The circumference is: ', sum(args))

triangle = Polygon(3, 1, 2, 3)

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.random.normal(loc=0, scale=0.5, size=1000)
y = np.random.normal(loc=0, scale = 0.5, size=1000)

plt.scatter(x, y)