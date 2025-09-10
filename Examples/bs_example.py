from Binomial_Trees import call_option, put_option

def main():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
    
    call = call_option(S, K, T, r, sigma, N=200, american=False)
    put = put_option(S, K, T, r, sigma, N=200, american=True)

    print(f"European Call (Binomial, N=200): {call}")
    print(f"American Put   (Binomial, N=200): {put}")

if __name__ == "__main__":
    main()