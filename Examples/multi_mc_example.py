from monte_carlo.MCmulti import monte_carlo_correlated_stocks

def main():
    S = [100, 120]              # initial prices
    mu = [0.05, 0.04]           # drifts
    sigma = [0.2, 0.25]         # volatilities
    corr_matrix = [[1.0, 0.7], 
                   [0.7, 1.0]]  # correlation matrix
    
    T, steps, num_paths = 1, 250, 5000

    means_correlated = monte_carlo_correlated_stocks(
        S, mu, sigma, corr_matrix, 
        T, steps, num_paths, plot_paths=20)

    print(f"Monte Carlo Simulated Mean: {means_correlated}")

if __name__ == "__main__":
    main()