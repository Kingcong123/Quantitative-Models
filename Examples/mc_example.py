from monte_carlo.MCsolo import monte_carlo_stock_paths

def main():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    steps, num_paths = 252, 10000

    mean = monte_carlo_stock_paths(S, K, T, r, sigma, steps, num_paths, plot_paths=10)

    print(f"Monte Carlo Simulated Mean: {mean}")

if __name__ == "__main__":
    main()

