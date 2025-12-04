import numpy as np

def antithetic_estimator(func, n_pairs=5000, *args, seed=None, **kwargs):
    rng = np.random.default_rng(seed)
    u = rng.normal(size=(n_pairs,)+kwargs.get('shape', (1,)))
    u_neg = -u
    est1 = func(u, *args)
    est2 = func(u_neg, *args)
    return 0.5*(est1 + est2)
