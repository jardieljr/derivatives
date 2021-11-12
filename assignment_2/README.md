# Financial Derivatives - group assginment 2-Option Pricing an American or exotic option 

## TSM project - M2 FiRE


Authors :
Ilyès BOUSSOUF;
Jardiel DA SILVA ARAUJO JUNIOR;
Nabiil BUDUREEA;
Huifen CHEN

**The Excel file to be used comprising our option pricing models can be found in the project repository and is titled *Derivatives_Project_File.xlsm***

# Momento
Like it was thoroughly substantiated in the last assignment, there are two types of options, Call options which allow the owner to buy the underlying asset at strike price stated in the contract within a specific timeframe. 
On the other hand, Put options allow the owner to sell the underlying asset at the strike price stated in the contract within a specific timeframe. 

A plethora of method exist to price options, for instance, as previously studied in the previous lectures and assignment, the Binomial tree calculates the value of an asset over a series of time steps. In this stepwise process, the asset price can go up or down based on the up and down probability. The value of the option is sequentially computed at each point in the tree, that is from the final to its initial point. 

In this vein, the objective of this assignment is based on the applications to the pricing of an American or Exotic option, using the Monte Carlo Simulations by the means of Excel and VBA. For our case, our focal point will be laid on American options. 



# Part I :  Asian option by given parameters 
In this part, we designed a binomial model by VBA with continuously compounded dividends to price an Asian option.

Asian option is one of the exotic option which based on the average price over some period of time, so it is an example of a path-dependent option. Normally, asian options are worth less than other equivalent ordinary options due to the less volatitly of the averaged price of the underlying asset.

֍The given parameters are following:

r = 1% (risk-free rate, continuously compounded)

σ = 20%(volitality)

δ = 3% (continuously compounded)

µ = 10% (expected return)

T= 1 month

n=30 (each period 1 day)

S0=$100

1)considering deviation of paying compounded dividend, we will model the stock returns of each period by u(up-factor per step) and d (down-factor per step) using the equations.
  
  
where r is the continuously compounded annual interest rate, δ is the continuous dividend yield, σ is the annual volatility, and h is the length of a binomial period in years.

We input the parameter and get u=xxxxx, d= xxxxx.

2)The risk-neutral probability fumula in one period is
 
 
where r is the continuously compounded annual interest rate, δ is the continuous dividend yield, h is the length of a binomial period in years. u and d are the up and down factor per period.  

We input the parameter and get p*=xxxxx.

3)According to the given formula, we use the arithmetic average of realized stock prices as the strike price on day K.

then the payoff of the call option:

xxxxx xxxxx

The call price will be:

xxxxx xxxxx

4)the heding ratio formula:


The option price and hedging ratio at all nodes of the binomial tree:

# Part II :  price an American Option 
In this part, we designed a VBA model to price an American option using binomial model and 
Monte carlo simulation(short for MCS) based on a continuous stochastic process(geometric brownian motion as in the Black-Merton-Scholes model)

1)The market price of the target asset ( apple, AAPL )is following:
Stock price =$xxx, Strike price=$xxx,quoted call price=$xxx
(K,T)=(xx,xx)  Matrurity time= 30 days

2)data collecation and computation of the characteristics of the stock

We calculate the daily return of XXX stock prices, and compute the daily volatility of the stock, then we use the formula(daily volatility * √252 ) to get the annual volatility XXX. So we set the annual volatility of the stock σ = XXX.

We get the dividend payments of XXX for the past 5 years, and calculate both the annual dividend yield and the average annual dividend yield. Further to get the compute the continuously compound dividend, we use δ = ln(average annual dividend yield) to get the continuously compound dividend yield. The continuously compound dividend of the stock δ = XXX. 

we choose SOFR monthly rate to be the risk free rate.

֍the main characteristics for the option 

Return µ =xxxx

Volitality σ =√252* daily volitality

continuously compounded dividend δ = xxxx

r = xx (risk-free rate, SOFR 3 MONTH)

T=  xx days

N=  xx (each period 1 day)

3)result price of american option using binomial model



4)result price of american option using Monte Carlo Simulation based on Black-Merton-Scholes model




5)Conclusion and Observations













