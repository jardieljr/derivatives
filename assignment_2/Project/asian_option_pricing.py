import numpy as np
# from brownian_motion_simulation import *



class AsianOption: 
    def __init__(self, M, K, option_side, S0, sigma, T, r, I):
        self.M = M
        self.K = K
        self.option=option_side
        self.S0 = S0
        self.sigma = sigma
        self.T = T
        self.r = r
        self.I = I
        self.dt = self.T/self.M
        
    def asian_option_pricing(self):

        self.S = np.zeros((int(self.M + 1), int(self.I)))    
        self.S[0] = self.S0
        
        for t in range(1, self.M + 1):
            self.S[t] = self.S[t - 1] * np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt 
                    + self.sigma * np.sqrt(self.dt) * np.random.standard_normal(self.I))
        
        # calculate payoff at maturity
        if self.option == 'Call':
            payOff = np.maximum(self.S.mean(axis=0) - self.K, 0) # Average of Stock Price taken on path for each dt timestamp
        else:
            payOff = np.maximum(self.K - self.S.mean(axis=0), 0) # Average of Stock Price taken on path for each dt timestamp
        
        # calculate MCS estimator
        optionPrice = np.exp(-self.r * self.T) * 1 / self.I * np.sum(payOff)
        
        return optionPrice
    
if __name__ == '__main__':
    
    x = AsianOption(100, 105, 'Call', 105, 0.2, 1, 0.01, 100000)
    
    result = x.asian_option_pricing()
