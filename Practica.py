import math
import numpy as np
import matplotlib.pyplot as plt

x = math.radians(47)
a = math.radians(45)

y = np.sin(x)

# Taylor series expansion of sin(x) around a = pi/4
p0 = round(math.sin(a),7)
p1 = round(p0 + math.cos(a) * (x - a),7)
p2 = round(p1 - (math.sin(a) / 2) * (x - a)**2,7)
p3 = round(p2 - (math.cos(a) / 6) * (x - a)**3,7)

print("Valor real de sen(47°):", math.sin(x))
print("-----------------------------------")
print("Aproximación P0:", p0)
print("Aproximación P1:", p1)
print("Aproximación P2:", p2)
print("Aproximación P3:", p3)

R0 = math.cos(a) * (x - a)
R1 = - (math.sin(a) / 2) * (x - a)**2
R2 = - (math.cos(a) / 6) * (x - a)**3

print("-----------------------------------")
print("Resto R0:", R0)
print("Resto R1:", R1)
print("Resto R2:", R2)