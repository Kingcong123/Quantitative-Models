from Black_Scholes import black_scholes_call, black_scholes_put

def main():
    # Example parameters
    S = 100     # current stock price
    K = 100     # strike price
    T = 1       # 1 year until maturity
    r = 0.05    # 5% risk-free rate
    sigma = 0.2 # 20% volatility
    
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)

    print("Black-Scholes Call Price: {call_price}")
    print("Black-Scholes Put Price: {put_price}")

    if __name__ == "__main__":
        main()