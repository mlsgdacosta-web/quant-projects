import numpy as np

def simulate_two_state(p=0.9, q=0.8, n=1000, seed=None):
    rng = np.random.default_rng(seed)
    states = np.zeros(n, dtype=int)
    for t in range(1, n):
        if states[t-1] == 0:
            states[t] = 0 if rng.random() < p else 1
        else:
            states[t] = 1 if rng.random() < q else 0
    return states

if __name__ == '__main__':
    s = simulate_two_state()
    print('Fraction in state 0:', (s==0).mean())
