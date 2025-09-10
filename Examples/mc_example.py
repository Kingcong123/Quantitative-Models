from monte_carlo.MCsolo import monte_carlo_stock_paths

def main():
    S, mu, T, sigma = 100, 0.05, 1, 0.2
    steps, num_paths = 252, 10000
    plot_paths = 20

    mean = monte_carlo_stock_paths(S, mu, T, sigma, steps, num_paths, plot_paths)

    print(f"Monte Carlo Simulated Mean: {mean}")

if __name__ == "__main__":
    main()

