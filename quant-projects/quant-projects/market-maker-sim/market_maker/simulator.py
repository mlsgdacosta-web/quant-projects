import numpy as np
from .order_book import SimpleOrderBook

def run_simulation(steps=1000, seed=None):
    rng = np.random.default_rng(seed)
    ob = SimpleOrderBook()
    mid = 100.0
    inventory = 0
    pnl = 0.0
    history = []
    for t in range(steps):
        # synthetic mid price moves as random walk
        mid += rng.normal(scale=0.05)
        # simple strategy: post bid/ask around mid
        bid = mid - 0.01
        ask = mid + 0.01
        # random fills
        if rng.random() < 0.01:
            inventory += 1
            pnl -= bid
        if rng.random() < 0.01:
            inventory -= 1
            pnl += ask
        # inventory penalty
        pnl_adj = pnl - 0.001*(inventory**2)
        history.append((t, mid, inventory, pnl_adj))
    return history

if __name__ == '__main__':
    h = run_simulation(steps=1000)
    print('Finished simulation with', len(h), 'steps')
