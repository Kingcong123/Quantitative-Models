import numpy as np
import numpy as np

def call_option(S, K, T, r, sigma, N = 100, american=False):
    """
    Parameters:
    S : initial stock price
    K : strike price
    T : time to maturity (in years)
    r : risk-free rate
    sigma : volatility
    N : number of steps in the tree
    american : True allows early exercise (American option)
    
    Returns:
    option price
    """
    #up, down, risk-neutral prob
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))     
    d = 1 / u                       
    q = (np.exp(r * dt) - d) / (u - d) 

    # Stock prices at maturity
    Stock_prices = S * (u ** np.arange(N, -1, -1)) * (d ** np.arange(0, N + 1, 1))
    option_values = np.maximum(Stock_prices - K, 0)

    # Compute backwards
    for i in range(N-1, -1, -1):
        Stock_prices = S * (u ** np.arange(i, -1, -1)) * (d ** np.arange(0, i + 1, 1)) #Stock prices at time i
        option_values = np.exp(-r * dt) * (q * option_values[:-1] + (1 - q) * option_values[1:])

        if american:
            option_values = np.maximum(option_values, Stock_prices - K)  # early exercise

    return option_values[0]


def put_option(S, K, T, r, sigma, N=100, american=False):
    """
    Same parameters as call_options
    """
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)

    Stock_prices = S * (u ** np.arange(N, -1, -1)) * (d ** np.arange(0, N + 1, 1))
    option_values = np.maximum(K - Stock_prices, 0)

    for i in range(N-1, -1, -1):
        Stock_prices = S * (u ** np.arange(i, -1, -1)) * (d ** np.arange(0, i + 1, 1))
        option_values = np.exp(-r * dt) * (q * option_values[:-1] + (1 - q) * option_values[1:])

        if american:
            option_values = np.maximum(option_values, K - Stock_prices)  # early exercise

    return option_values[0]