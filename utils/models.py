import numpy as np

def calc_returns(prices):
    return np.diff(prices) / prices[:-1] * 100

def compute_volatility(returns):
    return np.std(returns)

def compute_beta(btc_returns, alt_returns):
    if len(btc_returns) != len(alt_returns):
        raise ValueError("Mismatched return series length")
    covariance = np.cov(alt_returns, btc_returns)[0][1]
    variance = np.var(btc_returns)
    return covariance / variance if variance != 0 else 0
