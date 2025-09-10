
import numpy as np
import matplotlib.pyplot as plt
def monte_carlo_correlated_stocks(S, mu, sigma, corr_matrix, T, steps, num_paths = 10000, plot_paths = 10):
    """
    Parameters:
    - S: initial stock price (|S| = #stocks)
    - mu: drift (same length as |S|)
    - sigma: volatility (same length as |S|)
    - corr_matrix: correlation matrix (|S| x |S|) 
    - T: time horizon (in years)
    - steps: number of time steps
    - num_paths: number of simulated paths
    - plot_paths: number of paths to plot

    Returns:
    Array of predicted mean stock prices of the input stocks
    """
    
    paths = monte_carlo_correlated_sim(S, mu, sigma, corr_matrix, T, steps, num_paths = 10000)
    
    plot_stock_paths(paths, len(S), T, steps, num_paths, plot_paths)
    
    means = []
    for i in range(len(S)):
       means.append(np.mean[: , steps + 1, i])
    
    return means


def monte_carlo_correlated_sim(S, mu, sigma, corr_matrix, T, steps, num_paths = 10000,):
    """
    Simulate stock price paths using Geometric Brownian Motion (GBM).
    """
    dt = T / steps 
    S, mu, sigma = np.array(S), np.array(mu), np.array(sigma)
    num_stocks = len(S)

    L = np.linalg.cholesky(corr_matrix)

    paths = np.zeros((num_paths, steps + 1, num_stocks))
    paths[:, 0, :] = S
    
    for t in range(1, steps + 1):
        # Generate correlated random normals
        z = np.random.normal((num_paths, num_stocks))
        correlated_z = z @ L.T

        #GBM
        drift = (mu - 0.5 * sigma**2) * dt
        stochastic = sigma * np.sqrt(dt) * correlated_z
        paths[:, t, :] = paths[:, t-1, :] * np.exp(drift + stochastic)

    return paths



def plot_stock_paths(paths, num_stocks, T, steps, num_paths, plot_paths):
    "Plot plot_paths number of paths for each stock"

    time_grid = np.linspace(0, T, steps+1)
    plt.figure(figsize=(12, 6))

    for i in range(num_stocks):
        for j in range(min(plot_paths, num_paths)):
            plt.plot(time_grid, paths[j, :, i], lw=1, alpha=0.6)
        plt.title("Simulated Paths for Stock {i+1}")
        plt.xlabel("Time (Years)")
        plt.ylabel("Stock Price")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.show()

