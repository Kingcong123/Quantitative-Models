import numpy as np
from monte_carlo.MCmulti import monte_carlo_correlated_sim

def shock_volatility_and_simulate(S0, mu, sigma, corr, T, n_steps, n_paths,
                                  vol_multiplier=1.2, seed=None):
    """
    Re-run simulation with all volatilities scaled by vol_multiplier.
    Returns: paths (n_paths, n_steps+1, n_stocks)
    """
    sigma_shocked = np.array(sigma) * vol_multiplier
    return monte_carlo_correlated_sim(S0, mu, sigma_shocked, corr, T, n_steps, n_paths)


def shock_correlation_and_simulate(S0, mu, sigma, corr, T, n_steps, n_paths,
                                   off_diag_shift=0.1, seed=None):
    """
    Increase off-diagonal correlations by adding off_diag_shift,
    then clipping to [-0.999, 0.999] diagonals left at 1.
    Returns: paths using the shocked correlation matrix.
    """
    corr = np.array(corr).copy()
    n = corr.shape[0]
    for i in range(n):
        for j in range(n):
            if i != j:
                corr[i, j] = np.clip(corr[i, j] + off_diag_shift, -0.999, 0.999)
    # ensure symmetry and diagonals = 1
    corr = (corr + corr.T) / 2
    np.fill_diagonal(corr, 1.0)
    return monte_carlo_correlated_sim(S0, mu, sigma, corr, T, n_steps, n_paths)


def shock_price_drop_and_simulate(S0, mu, sigma, corr, T, n_steps, n_paths,
                                  immediate_drop_pct=0.2, seed=None):
    """
    Simulate as usual, but apply an immediate drop to initial prices (shock),
    = S0 * (1 - immediate_drop_pct)
    """
    S0_shocked = np.array(S0) * (1.0 - immediate_drop_pct)
    return monte_carlo_correlated_sim(S0_shocked, mu, sigma, corr, T, n_steps, n_paths, seed=seed)