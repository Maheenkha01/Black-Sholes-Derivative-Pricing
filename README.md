# Black-Sholes-Derivative-Pricing
Black-Sholes Derivative Pricing with Monte Carlo Simulaitons
Call Option Vs Stock Price 

<img width="563" height="453" alt="image" src="https://github.com/user-attachments/assets/1dee5e2b-d5a2-41fc-8877-9fc5fe253563" />

Delta Vs Stock Price

<img width="567" height="453" alt="image" src="https://github.com/user-attachments/assets/905116a0-3211-40d6-bc4f-3df7ed7f0415" />


 Key Insights
- Call option price increases with stock price
- Delta approaches:
  - 1 for deep in-the-money options
  - 0 for out-of-the-money options
- Higher volatility increases option value

  Limitations:
- Ignores transaction costs
- Assumes constant volatility
- Cannot capture market smiles/skews

Monte Carlo Simulations 

<img width="580" height="453" alt="image" src="https://github.com/user-attachments/assets/5e451791-7b83-4be6-9072-ec5fb5c06a23" />

Monte Carlo Simulation vs Black-Sholes Price Formula

<img width="594" height="453" alt="image" src="https://github.com/user-attachments/assets/6a5f67ea-c289-4985-934a-6631eeddb146" />

Key Findings
- Monte Carlo converges to Black-Scholes price as simulations increase
- Antithetic variates reduce variance → more stable estimates
- Monte Carlo is flexible and can handle:
  - Path-dependent options
  - Complex payoffs

Limitations
- Computationally expensive
- Slow convergence (O(1/√N))

Monte Carlo Simulations and Stock Price Paths

<img width="571" height="453" alt="image" src="https://github.com/user-attachments/assets/354d9542-3d3d-468c-97c7-4f60f5d6ba65" />



