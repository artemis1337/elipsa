import matplotlib.pyplot as plt
import numpy as np
import math
pi = math.pi
from sympy import *

# Krog s polmerom R sestavljen iz N točk
R = 1
N = 300
def PointsInCircum(r,n=100):
    x = []
    y = []
    for i in range (0, n+1):
        x.append(round((math.cos(2*pi/n*i)*r),2))
        y.append(round((math.sin(2*pi/n*i)*r),2))

    return x, y

x, y = PointsInCircum(R, N)

coords = np.array([[0], [0], [1]])

for i in range(0, len(x)):
    newColumn = [[x[i]], [y[i]], [1]]
    coords = np.append(coords, newColumn, axis=1)


# Risanje grafa

def grid_plotter(points, labels, title=""):
    markers = ['o', 'o', 's', '^', 'p', 'v']
    fig, ax = plt.subplots(figsize=(7,7))
    for i, p in enumerate(points):
        x, y = p[0], p[1]
        ax.scatter(x, y, label=labels[i], marker=markers[i], alpha=0.4, s=10)
    ax.legend(loc='lower right')
    lim = 7
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)

    plt.title(title)

    ax.grid(True)
    plt.show()

# Definicija transformacij
def get_rotation(angle):
    angle = np.radians(angle)
    return np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle),  np.cos(angle), 0],
        [0, 0, 1]
    ])
def get_translation(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def get_scale(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

# ==========================================
alpha_deg = 30
alpha = rad(alpha_deg)
R1 = get_rotation(alpha_deg)

a = 3
b = 1
S1 = get_scale(a, b)

p = 0
q = 0
T1 = get_translation(p, q)


coords_rotate = R1 @ coords
coords_scale = S1 @ coords 
coords_translate = T1 @ S1 @ coords
coords_change = R1 @  S1 @ coords

x, y = symbols('x y')

# Formula za navadnen premik in razteg
formula = str(expand_power_exp(((x-p) **2) /((a*R)**2) + ((y-q)**2)/((b*R)**2))) + " = 1"

# FORMULE ZA ROTIRANJE POSTRANI (ne vem, če je pravilno)
# X smer: x + p
# ((x + p) * cos(alpha) + (y+q) * sin(alpha))
# # Y smer: n
# ((x + p) * sin(alpha) - (y+q) * cos(alpha))
# 
# Formula za premik, razteg in rotacijo
formula = str(expand(((((x + p) * cos(alpha) + (y+q) * sin(alpha))) **2) /((a*R)**2) + 
        ((((x + p) * sin(alpha) - (y+q) * cos(alpha)))**2)/((b*R)**2))) + " = 1"


print("formula:", formula)

grid_plotter([coords, coords_change], 
labels=["original", "razteg in rotacija"], title=formula)