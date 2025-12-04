import numpy as np

def simulate_garch(n=1000, omega=0.1, alpha=0.1, beta=0.8, seed=None):
    rng = np.random.default_rng(seed)
    eps = np.zeros(n)
    sigma2 = np.zeros(n)
    sigma2[0] = omega / (1 - alpha - beta)
    for t in range(1, n):
        z = rng.normal()
        eps[t] = z * np.sqrt(sigma2[t-1])
        sigma2[t] = omega + alpha*eps[t]**2 + beta*sigma2[t-1]
    return eps, sigma2
