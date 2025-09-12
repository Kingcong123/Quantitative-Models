This repository contains beginner-friendly implementations of common option pricing models in Python.  
The project is organized into three main modules:

- **Black-Scholes**: Closed-form solutions for European call and put options.
- **Binomial Tree**: Step-by-step discrete-time pricing for call and put options (works for both European and American).
- **Monte Carlo**: Simulation-based pricing methods for single stocks and correlated assets.

---

## Features

- Black–Scholes pricing for European calls and puts  
- Binomial tree pricing with support for American options  
- Monte Carlo simulation of stock paths using Geometric Brownian Motion (GBM)  
- Correlated stock simulations with Cholesky decomposition  
- Plotting utilities for simulated paths  
-Portfolio risk metrics: Value-at-Risk (VaR) and Conditional VaR (CVaR)
-Stress testing with shocks to volatility and correlations