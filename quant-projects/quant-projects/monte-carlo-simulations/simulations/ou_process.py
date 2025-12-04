import numpy as np

def simulate_ou(X0=0.0, theta=1.0, mu=0.0, sigma=0.2, T=1.0, steps=252, n_paths=1000, seed=None):
    rng = np.random.default_rng(seed)
    dt = T/steps
    X = np.zeros((n_paths, steps+1))
    X[:,0] = X0
    for t in range(1, steps+1):
        X[:,t] = X[:,t-1] + theta*(mu - X[:,t-1])*dt + sigma*np.sqrt(dt)*rng.normal(size=n_paths)
    return X
