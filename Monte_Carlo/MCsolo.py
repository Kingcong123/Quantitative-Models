import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_stock_paths(S, mu, sigma, T, steps, num_paths = 10000, plot_paths = 10):
    """
    Simulate stock price paths using Geometric Brownian Motion (GBM).
    Parameters:
    - S: initial stock price
    - mu: drift
    - sigma: volatility
    - T: time horizon (in years)
    - steps: number of time steps
    - num_paths: number of simulated paths
    - plot_paths: number of paths to plot
    """
    np.random.seed(None) 
    paths = monte_carlo_simulation(S, mu, sigma, T, steps, num_paths)
    plot_stock_paths(T, steps, paths, plot_paths)
    return np.mean(paths[:, steps])

def monte_carlo_simulation(S, mu, sigma, T, steps, num_paths):
    """
    Same parameters as monte_carlo_stock_paths
    """
    dt = T / steps
    paths = np.zeros((num_paths, steps + 1))
    paths[:, 0] = S

    for t in range(1, steps + 1):
        z = np.random.standard_normal(num_paths) 
        paths[:, t] = paths[:, t-1] * np.exp((mu - 0.5 * sigma**2) * dt +
                                             sigma * np.sqrt(dt) * z)

    return paths


def plot_stock_paths(T, steps, paths, plot_paths):
    """
    Same parameters as monte_carlo_stock_paths
    """
    num_paths, steps_plus_1 = paths.shape
    steps = steps_plus_1 - 1
    time_grid = np.linspace(0, T, steps + 1)

    plt.figure(figsize=(10,6))
    for i in range(min(num_paths, plot_paths)):  # plot up to 10 sample paths
        plt.plot(time_grid, paths[i], lw=1)
    plt.title("Monte Carlo Simulated Stock Price Paths")
    plt.xlabel("Time (Years)")
    plt.ylabel("Stock Price")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()