import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def firtsttask(x, y, alpha):
    R = np.array([[math.cos(alpha), math.sin(-1*alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
    M_positive = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])
    M_negative = np.array([[1, 0, -1*x], [0, 1, -1*y], [0, 0, 1]])
    A = M_positive.dot(R)
    A = A.dot(M_negative)
    return A

def secondtask(xa, ya, za, xb, yb, zb, xc, yc, zc):

    ny = (zb - za) * (xc - xa) - (zc - za) * (xb - xa)
    nz = -((yb - ya) * (xc - xa) - (yc - ya) * (xb - xa))
    nx = -(nz * (zb - za) + ny * (yb - ya)) / (xb - xa)

    check = -(nz * (zc - za) + ny * (yc - ya)) / (xc - xa)

    if check != nx:
        print('Error')
    else:
        return nx, ny, nz


def thirdtask(xa, ya, za, xb, yb, zb, xc, yc, zc, x, y):
    First = (xa - x) * (yb - ya) - (xb - xa) * (ya - y)
    Second = (xb - x) * (yc - yb) - (xc - xb) * (yb - y)
    Third = (xc - x) * (ya - yc) - (xa - xc) * (yc - y)
    if (First < 0) and (Second < 0) and (Third < 0):
        return True
    else:
        return False

if __name__ == '__main__':
    print ('First task:')
    print(firtsttask(1,1,0.785))
    print('Second task:')
    print(secondtask(0, 0, 31, 10, 21, 0, 19, 10, 0))
    print('Third task:')
    print(thirdtask(0, 0, 31, 10, 21, 0, 19, 10, 0, 1, 10))
