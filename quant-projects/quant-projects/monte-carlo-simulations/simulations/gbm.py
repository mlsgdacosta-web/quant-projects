import numpy as np

def simulate_gbm(S0=100, mu=0.05, sigma=0.2, T=1.0, steps=252, n_paths=10000, seed=None):
    rng = np.random.default_rng(seed)
    dt = T/steps
    increments = rng.normal(loc=(mu - 0.5*sigma**2)*dt, scale=sigma*np.sqrt(dt), size=(n_paths, steps))
    log_paths = np.cumsum(increments, axis=1)
    S = S0 * np.exp(log_paths)
    S = np.concatenate([np.full((n_paths,1), S0), S], axis=1)
    return S

if __name__ == '__main__':
    paths = simulate_gbm(n_paths=1000)
    print('Simulated GBM shape:', paths.shape)
