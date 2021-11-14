def american_option_pricing(K, option='call'):

    S = np.zeros((M + 1, I))    
    S[0] = S0
    df = np.exp(-r*dt)
    
    for t in range(1, M + 1):
        S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt 
                + sigma * np.sqrt(dt) * np.random.standard_normal(I))
    
    # calculate payoff at maturity
    if option == 'call':
        payOff = np.maximum(S - K, 0)
    else:
        payOff = np.maximum(K - S, 0)
        
    # LSM algorithm
    V = np.copy(payOff)
    for t in range(M - 1, 0, -1):
        reg = np.polyfit(S[t], V[t + 1] * df, 7) # Using 7 degree of freedom to find the continuation value for Option Price
        C = np.polyval(reg, S[t])
        
        # If Continuation value > Payoff then take discounted value of pay off at T+1 else take pay off value at time T
        V[t] = np.where(C > payOff[t], V[t + 1] * df, payOff[t]) 
    
    # calculate MCS estimator
    optionPrice = df * 1 / I * np.sum(V[1])
    
    return optionPrice
