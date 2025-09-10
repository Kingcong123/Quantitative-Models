from Monte_Carlo import monte_carlo_stock_paths

def main():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    steps, num_paths = 252, 10000

    call_price, put_price = monte_carlo_stock_paths(S, K, T, r, sigma, steps, num_paths, plot_paths=10)

    print("Monte Carlo Call Price: {call_price:.4f}")
    print("Monte Carlo Put Price:  {put_price:.4f}")

if __name__ == "__main__":
    main()