import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm 

def portfolio_pnl_from_paths(paths, weights):
    """
    Compute portfolio P&L from simulated paths.
    - paths: (n_paths, n_steps+1, n_stocks)
    - weights: vector of portfolio weights (same length as n_stocks),
      weights represent amounts in units of each asset or proportions multiplied by notional.
      This function interprets weights as *holdings* (not proportions) 
      initial value = S0 @ weights.
    Returns:
    - pnl: array length n_paths of final - initial portfolio value
    """
    weights = np.array(weights)
    initial = paths[0, 0, :] @ weights  # same initial across all paths
    final = paths[:, -1, :] @ weights   # (n_paths,)
    pnl = final - initial
    return pnl


def historical_var_cvar(pnl, confidence=0.95):
    """
    Historical VaR and CVaR based on simulated pnl.
    - confidence: e.g. 0.95 for 95% VaR
    Interpretation:
      - Loss = -pnl
      - VaR = loss at the confidence level (positive number)
      - CVaR = average loss beyond VaR
    Returns: (VaR, CVaR)
    """
    losses = -pnl  # positive numbers are losses
    alpha_pct = confidence * 100
    VaR = np.percentile(losses, alpha_pct)
    tail_losses = losses[losses >= VaR]
    CVaR = tail_losses.mean() if tail_losses.size > 0 else VaR
    return VaR, CVaR


def parametric_var(pnl, confidence=0.95):
    """
    Parametric (normal) VaR: assumes pnl ~ N(mu, sigma)
    Returns VaR (positive number representing loss) and CVaR using normality approximation.
    (This is a strong assumption)
    """
    mu = pnl.mean()
    sigma = pnl.std(ddof=1)
    z = norm.ppf(confidence)  # z_{alpha}
    # We want VaR as a positive loss value such that P(loss <= VaR) = confidence
    # loss = -pnl. So VaR_loss = - (mu + sigma * z)
    VaR = -(mu + sigma * z)
    # CVaR (ES) for normal can be computed analytically:
    lambda_ = norm.pdf(z) / (1 - confidence)
    CVaR = -(mu + sigma * lambda_)
    return VaR, CVaR


def plot_pnl_distribution(pnl, confidence_levels=(0.95, 0.99), bins=80, figsize=(10, 6)):
    """
    Plot histogram of profits and losses.
    """
    losses = -pnl
    plt.figure(figsize=figsize)
    plt.hist(losses, bins=bins, alpha=0.7, edgecolor="k")
    plt.title("Portfolio Loss Distribution (negative P&L)")
    plt.xlabel("Loss")
    plt.ylabel("Frequency")

    colors = ["C1", "C2", "C3"]
    for i, conf in enumerate(confidence_levels):
        VaR, CVaR = historical_var_cvar(pnl, confidence=conf)
        plt.axvline(VaR, color=colors[i % len(colors)], linestyle="--", lw=2,
                    label=f"VaR {int(conf*100)}% = {VaR:.2f}")
        plt.axvline(CVaR, color=colors[i % len(colors)], linestyle="-.", lw=2,
                    label=f"CVaR {int(conf*100)}% = {CVaR:.2f}")

    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()