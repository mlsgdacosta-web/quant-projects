import numpy as np

def difference(series, d=1):
    s = np.array(series)
    for _ in range(d):
        s = s[1:] - s[:-1]
    return s

def fit_arima_simple(series, p=1, d=1, q=0):
    # very small illustrative OLS-style AR(1) fit when p=1, q=0
    y = difference(series, d)
    x = y[:-1]
    y1 = y[1:]
    phi = np.sum(x*y1) / np.sum(x*x)
    resid = y1 - phi*x
    sigma2 = np.var(resid, ddof=1)
    return {"phi": phi, "sigma2": sigma2}
