import numpy as np

def revenue(q, price_func, cost_func):
    p = price_func(q)
    return p*q - cost_func(q)

def solve_pricing(K=20, price_func=lambda q: 10 - 0.1*q, cost_func=lambda q: 0.0, grid=100):
    qs = np.linspace(0.0, K, grid)
    vals = [revenue(q, price_func, cost_func) for q in qs]
    idx = int(np.argmax(vals))
    return qs[idx], vals[idx]

if __name__ == '__main__':
    q_opt, val = solve_pricing()
    print('q*', q_opt, 'value', val)
