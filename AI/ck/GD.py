import numpy as np
import math

# Hàm ban đầu
def cost(x):
    return x**2 + 5*np.sin(x)

# Đạo hàm
def grad(x):
    return 2*x + 5*np.cos(x)

def GD(x0, alpha = 0.1, esilon = 1e-3, loop= 10000):
    x = x0
    for i in range(loop):
        x = x - alpha * grad(x)
        if abs(grad(x)) < esilon:
            break
    return x

min = GD(-5)
print('Giá trị nhỏ nhất của hàm số là: ', cost(min), 'tại x = ', min)
