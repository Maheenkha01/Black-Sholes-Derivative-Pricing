# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:43:50 2026

@author: abdul
"""
""""
Black-Scholes Option Pricing Model

This project implements the Black-Scholes model for pricing European options.

 Objectives
- Derive and implement the Black-Scholes formula
- Visualise option prices
- Compute Greeks (Delta, Gamma, Vega)
- Analyse sensitivity to key parameters

 Applications
- Option pricing
- Risk management
- Dynamic hedging

 Black-Scholes Assumptions

The Black-Scholes model assumes:

1. Stock prices follow a Geometric Brownian motion
2. Volatility is constant
3. Interest rate is constant
4. No arbitrage opportunities
5. Markets are frictionless (no transaction costs)
6. European-style options (exercise only at maturity)


## Black-Scholes Formula

For a European Call Option:

C = S * N(d1) - K * e^{-rT} * N(d2)

Where:

d1 = [ln(S/K) + (r + σ²/2)T] / (σ√T)  
d2 = d1 - σ√T  

Parameters:
- S = stock price
- K = strike price
- T = time to maturity
- r = risk-free rate
- σ = volatility
###############
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Call Option 
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    return call

## Put Option 
def black_scholes_put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    put = K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put

##example
S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

call_price = black_scholes_call(S, K, T, r, sigma)
put_price = black_scholes_put(S, K, T, r, sigma)


print("Call Price:", call_price)
print("Put Price:", put_price)

"""
Call Price: 10.450583572185565

Put Price: 5.573526022256971
"""
## Option Price Sensitivity to Stock Price
#We analyse how the option value changes with the underlying asset price.

S_range = np.linspace(50, 150, 100)

call_prices = [black_scholes_call(S, K, T, r, sigma) for S in S_range]

plt.plot(S_range, call_prices)
plt.xlabel("Stock Price")
plt.ylabel("Call Price")
plt.title("Call Option Price vs Stock Price")
plt.grid()
plt.show()

"""

#### 
Option Greeks

Greeks measure sensitivity of option price:

- Delta → sensitivity to stock price
- Gamma → curvature
- Vega → sensitivity to volatility
"""
def delta_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    return norm.cdf(d1)

def gamma(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2)*T) / (sigma * np.sqrt(T))
    return S * norm.pdf(d1) * np.sqrt(T)


deltas = [delta_call(S, K, T, r, sigma) for S in S_range]

plt.plot(S_range, deltas)
plt.xlabel("Stock Price")
plt.ylabel("Delta")
plt.title("Delta vs Stock Price")
plt.grid()
plt.show()


"""
## Key Insights

- Call option price increases with stock price
- Delta approaches:
  - 1 for deep in-the-money options
  - 0 for out-of-the-money options
- Higher volatility increases option value

## Limitations

- Assumes constant volatility
- Ignores transaction costs
- Cannot capture market smiles/skews
""

""
Monte Carlo Simulations on European Call Option
"""
def monte_carlo_call(S, K, T, r, sigma, n_sim=10000):
    Z = np.random.normal(0, 1, n_sim)
    
    ST = S * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    
    payoff = np.maximum(ST - K, 0)
    
    price = np.exp(-r*T) * np.mean(payoff)
    
    return price
#Example
S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

mc_price = monte_carlo_call(S, K, T, r, sigma, 100000)

print("Monte Carlo Call Price:", mc_price)

"""
Comparing with Black-Sholes
"""

def bs_call(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)

bs_price = bs_call(S, K, T, r, sigma)

print("Black-Scholes Price:", bs_price)
print("Monte Carlo Price:", mc_price)
"""
###Output
Black-Scholes Price: 10.450583572185565
Monte Carlo Price: 10.497962498328807
""
Visualisation 
""""

Z = np.random.normal(0, 1, 100000)
ST = S * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)

plt.hist(ST, bins=50)
plt.title("Distribution of Simulated Stock Prices")
plt.xlabel("Stock Price at Maturity")
plt.ylabel("Frequency")
plt.show()

"""
Convergence of Monte Carlo Estimator

We analyse how the estimate converges as the number of simulations increases.
"""

simulations = np.arange(1000, 50000, 2000)
prices = []

for n_sim in simulations:
    prices.append(monte_carlo_call(S, K, T, r, sigma, n_sim))

plt.plot(simulations, prices, label="Monte Carlo")
plt.axhline(y=bs_price, color='r', linestyle='--', label="Black-Scholes")

plt.xlabel("Number of Simulations")
plt.ylabel("Option Price")
plt.title("Monte Carlo Convergence")
plt.legend()
plt.show()

def simulate_paths(S, T, r, sigma, steps=100, n_paths=20):
    dt = T / steps
    paths = np.zeros((steps, n_paths))
    paths[0] = S
    
    for t in range(1, steps):
        Z = np.random.normal(size=n_paths)
        paths[t] = paths[t-1] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z)
    
    return paths
"### Path Simulation "

paths = simulate_paths(S, T, r, sigma)

plt.plot(paths)
plt.title("Simulated Stock Price Paths")
plt.xlabel("Time Steps")
plt.ylabel("Stock Price")
plt.show()


"## Variance Reduction "
def monte_carlo_antithetic(S, K, T, r, sigma, n_sim=10000):
    Z = np.random.normal(0, 1, n_sim)
    Z_antithetic = -Z
    
    ST1 = S * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
    ST2 = S * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z_antithetic)
    
    payoff = (np.maximum(ST1 - K, 0) + np.maximum(ST2 - K, 0)) / 2
    
    price = np.exp(-r*T) * np.mean(payoff)
    
    return price
""" Comparison """

mc_basic = monte_carlo_call(S, K, T, r, sigma, 10000)
mc_anti = monte_carlo_antithetic(S, K, T, r, sigma, 10000)

print("Basic MC:", mc_basic)
print("Antithetic MC:", mc_anti)
print("Black-Scholes:", bs_price)

"""Outputs
Basic MC: 10.568656921612513
Antithetic MC: 10.4096412978107
Black-Scholes: 10.450583572185565
""

## Key Findings

- Monte Carlo converges to Black-Scholes price as simulations increase
- Antithetic variates reduce variance → more stable estimates
- Monte Carlo is flexible and can handle:
  - Path-dependent options
  - Complex payoffs

## Limitations

- Computationally expensive
- Slow convergence (O(1/√N))
""""
THANKYOU