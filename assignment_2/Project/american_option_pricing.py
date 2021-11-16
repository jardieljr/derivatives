import numpy as np

 
# S0 = 114.9 #Stock Price
# r = 0.0159 #risk free rate
# sigma = 0.1965 #Stock Constant Volatility
# T = 1.1 #Time for expiry
# I = 10000 #Number of simulations
# M = 50 #Time Steps for simulations
# dt = T/M #discrete time interval
# K = 100


class AmericanOption:
    
    def __init__(self,  M, K, option_side, S0, sigma, T, r, I):
        
        self.M = M
        self.K = K
        self.option=option_side
        self.S0 = S0
        self.sigma = sigma
        self.T = T
        self.r = r
        self.I = I
        self.dt = self.T/self.M
   
    
        
    def american_option_pricing(self):
        
        S = np.zeros((self.M + 1, self.I))    
        S[0] = self.S0
        df = np.exp(-self.r*self.dt)
        
        for t in range(1, self.M + 1):
            S[t] = S[t - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt 
            + self.sigma * np.sqrt(self.dt) * np.random.standard_normal(self.I))
        
        # calculate payoff at maturity
        if self.option == 'Call':
            payOff = np.maximum(S - self.K, 0)
        else:
            payOff = np.maximum(self.K - S, 0)
        
        # LSM algorithm
        V = np.copy(payOff)
        for t in range(self.M - 1, 0, -1):
            reg = np.polyfit(S[t], V[t + 1] * df, 7) # Using 7 degree of freedom to find the continuation value for Option Price
            C = np.polyval(reg, S[t])
        
        # If Continuation value > Payoff then take discounted value of pay off at T+1 else take pay off value at time T
            V[t] = np.where(C > payOff[t], V[t + 1] * df, payOff[t]) 
        
        # calculate MCS estimator
        optionPrice = df * 1 / self.I * np.sum(V[1])
        
        return optionPrice


    

if __name__ == '__main__':
    
    pass
    
    # x = american_option_pricing_using_gbm(100, option='call')

    # x = AmericanOption(M, K, "Call", S0, sigma, T, r, I)
    
    # p = x.american_option_pricing()
    
    # I = 10000
    # M = 50
   
    # S = np.zeros((M + 1, I))
    # S[0] = S0
