from Monte_Carlo import monte_carlo_stock_paths

def main():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    steps, num_paths = 252, 10000

    mean = monte_carlo_stock_paths(S, K, T, r, sigma, steps, num_paths, plot_paths=10)

    print(f"Monte Carlo Simulated Mean: {mean}")

if __name__ == "__main__":
    main()

from Monte_Carlo import monte_carlo_correlated_stocks

def main():
    S = [100, 120]              # initial prices
    mu = [0.05, 0.04]           # drifts
    sigma = [0.2, 0.25]         # volatilities
    corr_matrix = [[1.0, 0.7], 
                   [0.7, 1.0]]  # correlation matrix
    
    T, steps, num_paths = 1, 252, 5000

    means_correlated = monte_carlo_correlated_stocks(
        S, mu, sigma, corr_matrix, 
        T, steps, num_paths, plot_paths=5, seed=42)

    print(f"Monte Carlo Simulated Mean: {means_correlated}")

if __name__ == "__main__":
    main()