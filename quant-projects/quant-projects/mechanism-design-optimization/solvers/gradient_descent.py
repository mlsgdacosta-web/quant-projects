import numpy as np

def gradient_descent(func, x0, lr=1e-3, steps=1000):
    x = x0
    for i in range(steps):
        eps = 1e-6
        grad = (func(x+eps) - func(x-eps))/(2*eps)
        x = x + lr*grad
    return x
