from Black_Scholes.BS_pricing import black_scholes_call, black_scholes_put

def main():
    # Example parameters
    S = 100     # current stock price
    K = 100     # strike price
    T = 1       # 1 year until maturity
    r = 0.05    # 5% risk-free rate
    sigma = 0.2 # 20% volatility
    
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)

    print(f"Black-Scholes Call Price: {call_price}") #10.450583572185565
    print(f"Black-Scholes Put Price: {put_price}") # 5.573526022256971

if __name__ == "__main__":
    main()