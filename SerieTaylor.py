import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi/2, 400)
a = np.pi/4

y = np.sin(x)

# Taylor series expansion of sin(x) around a = pi/4

p0 = math.sin(a)
p1 = math.cos(a) * (x - a)
p2 = -math.sin(a) * (x - a)**2 / 2
p3 = math.cos(a) * (x - a)**3 / 6

print("p0:", p0)
print("p1:", p1)    
print("p2:", p2)
print("p3:", p3)
