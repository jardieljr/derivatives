# Derivatives - Option Pricing

TSM project - M2 FiRE

Authors :
Ilyès BOUSSOUF;
Jardiel DA SILVA ARAUJO JUNIOR;
Nabiil BUDUREEA;
Huifen Chen;


Momento :

Before digging into the principles of our group assignment, let us have a quick momento on some pertinent course materials viewed in the previous lectures. Options, in finance, are financial derivatives, that convey its owner the right but not the obligation to buy or sell the underlying asset, leaving the other counterparty of the contract with the obligation to execute if the holder decides to execute his option.

There are two types of options, Call options which allow the owner to buy the underlying asset at strike price stated in the contract within a specific timeframe, and Put options that allow the owner to sell the underlying asset at the strike price stated in the contract within a specific timeframe.

Options remain a very strong financial tool, as they provide increased cost efficiency, and they may be less risky than equity. They are mainly used for hedging and speculation purposes.
 
In the implementation of our model, we will focus on European Options. European options are a version of options contract that unlike the American style options limits its execution to its maturity date. In other words, the holder of a European call or put option can not exercise his option whenever he wants but only at the expiration date specified in the contract.

Our aim with this model is to price European Call and Put Options only by using some information that is related to the option contract and the underlying asset, such as the strike price, the maturity date, the spot price of the asset. etc, by implementing them in the Binomial and Black-Scholes-Merton formula.

Since options are derivatives contracts, the movement in the price of the underlying asset up or down has a direct but not a proportional effect on the price of the option. That is why, these different pricing models are based also on other determining price factors, such as interest rates, risk-free rates, volatility, etc.

The document is structured as follows: the first part will discuss on the overview of the questions, the second part will explain the foundations of the Binomial and Black-Scholes-Merton model and a third part that will be a User Guide for the excel model.

Foundations of the Black-Scholes-Merton formula:

The Black-Scholes is a pricing model used to determine the fair price or theoretical value for a call or a put option based on six variables such as volatility, type of option, underlying stock price, time, strike price, and the risk-free rate. The quantum of speculation is more in the case of stock market derivatives, and hence proper pricing of options eliminates the opportunity for any arbitrage (The Economics Times). The use of this model is for the determination of a European call option, leading to the fact that the latter can be exercised only at the date of expiration.

The assumptions of the Black-Scholes-Merton model:

This option pricing model relies on a plethora of assumptions. Some of them are assumptions are the same as in financial models such as Sharpe (1964), Lintner (1965), and Mossin (1966) Capital Asset Pricing Model (CAPM) and some of them are different from the latter.
The elementary assumptions for the Black-Scholes model to be satisfied are as follows:
	The fact that there are no restrictions, taxes, and limitations on security tradings, these security markets are frictionless. 
	During the lifetime of the option, there are no additional payments from the underlying assets
	The risk-free interest rate is constant for the whole lifespan of the option, thus investors can borrow or lend at that same rate
	No riskless arbitrage opportunities
	Continuous trading in assets throughout time
	The price of the underlying asset has a lognormal distribution and evolves with continuous sample paths according to the Brownian motion process
	More is preferred to less by investors and they agree on the function of underlying asset’s variance σ2, which is considered to be constant

Considering the fact that these assumptions are satisfied, the Black-Scholes formula is obtained.
The mathematical formulae applied for both a call and a put option and it is as follows:

![Screenshot](Form2_Github.png)

where

![Screenshot](Form2_Github.png)

with :

●	N(𝑥) is the cumulative probability function for a variable with standard normal distribution N(0,1) with a mean of 0 and a variance of 1.




