import numpy as np
import brownian_motion_simulation as brow

def asian_option_pricing(K, option='call'):

    S = np.zeros((M + 1, I))    
    S[0] = S0
    
    for t in range(1, M + 1):
        S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt 
                + sigma * np.sqrt(dt) * np.random.standard_normal(I))
    
    # calculate payoff at maturity
    if option == 'call':
        payOff = np.maximum(S.mean(axis=0) - K, 0) # Average of Stock Price taken on path for each dt timestamp
    else:
        payOff = np.maximum(K - S.mean(axis=0), 0) # Average of Stock Price taken on path for each dt timestamp
    
    # calculate MCS estimator
    optionPrice = np.exp(-r * T) * 1 / I * np.sum(payOff )
    
    return optionPrice
