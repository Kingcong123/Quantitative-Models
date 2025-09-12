import numpy as np
from VAR_model import portfolio_risk, stress_testers
from monte_carlo import MCmulti

def main():
    # portfolio example: 2 assets
    S0 = [100.0, 120.0]
    mu = [0.05, 0.03]
    sigma = [0.2, 0.25]
    corr = np.array([[1.0, 0.5], [0.5, 1.0]])
    weights = np.array([1.0, 1.0])
    T = 1.0
    n_steps = 250
    n_paths = 20000

    # Simulation
    seed = 100
    paths = MCmulti.monte_carlo_correlated_sim(S0, mu, sigma, corr, T, n_steps, n_paths, seed)
    pnl = portfolio_risk.portfolio_pnl_from_paths(paths, weights)

    # compute historical VaR and CVaR
    for conf in (0.95, 0.99):
        VaR, CVaR = portfolio_risk.historical_var_cvar(pnl, confidence=conf)
        print(f"Historical VaR {int(conf*100)}%: {VaR:.2f}, CVaR: {CVaR:.2f}")

    # parametric VaR example
    pVaR, pCVaR = portfolio_risk.parametric_var(pnl, confidence=0.95)
    print(f"Parametric VaR 95%: {pVaR:.2f}, Parametric CVaR (normal approx): {pCVaR:.2f}")

    # plot loss distribution with VaR/CVaR lines
    portfolio_risk.plot_pnl_distribution(pnl, confidence_levels=(0.95, 0.99))

    # a simple stress test: 50% vol spike
    paths_vol_spike = stress_testers.shock_volatility_and_simulate(S0, mu, sigma, corr, T, n_steps, n_paths,
                                                    vol_multiplier=1.5)
    pnl_vol_spike = portfolio_risk.portfolio_pnl_from_paths(paths_vol_spike, weights)
    VaR_spike, CVaR_spike = portfolio_risk.historical_var_cvar(pnl_vol_spike, confidence=0.95)
    print(f"After vol x1.5 shock: VaR95={VaR_spike:.2f}, CVaR95={CVaR_spike:.2f}")

    # correlation stress: correlations +0.3
    paths_corr = stress_testers.shock_correlation_and_simulate(S0, mu, sigma, corr, T, n_steps, n_paths,
                                                off_diag_shift=0.3)
    pnl_corr = portfolio_risk.portfolio_pnl_from_paths(paths_corr, weights)
    VaR_corr, CVaR_corr = portfolio_risk.historical_var_cvar(pnl_corr, confidence=0.95)
    print(f"After corr +0.3 shock: VaR95={VaR_corr:.2f}, CVaR95={CVaR_corr:.2f}")

    # immediate price shock (20% drop)
    paths_price_drop = stress_testers.shock_price_drop_and_simulate(S0, mu, sigma, corr, T, n_steps, n_paths,
                                                     immediate_drop_pct=0.20)
    pnl_price_drop = portfolio_risk.portfolio_pnl_from_paths(paths_price_drop, weights)
    VaR_drop, CVaR_drop = portfolio_risk.historical_var_cvar(pnl_price_drop, confidence=0.95)
    print(f"After immediate -20% price shock: VaR95={VaR_drop:.2f}, CVaR95={CVaR_drop:.2f}")

if __name__ == "__main__":
    main()