# OverSold-Indicator
The term "oversold" refers to a condition where an asset has traded lower in price and has the potential for a price bounce. Here is a list of indicators of over-sold equities and their easy python implementations. There are plenty of indicators for traders to identify oversold stocks, including P/E ratio, RSI, and KDJ, which are used as signals for longing stocks. 

1. RSI (relative strength index): 
The relative strength index (RSI) is a momentum indicator that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or other asset. [Reference 1](https://www.investopedia.com/terms/r/rsi.asp) When RSI is lower than 25%, it is considered oversold. [Reference 2](https://baike.baidu.com/item/%E8%B6%85%E5%8D%96/3692257)

[What are the best indicators for oversold?](https://www.investopedia.com/ask/answers/121214/what-are-best-indicators-identify-overbought-and-oversold-stocks.asp)

2. [KDJ curves:](https://en.wikipedia.org/wiki/Stochastic_oscillator)
In technical analysis of securities trading, the stochastic oscillator is a momentum indicator that uses support and resistance levels.

``%K=100*(Price-L5)/(H5-L5)``
``%D=((K1+K2+K3)/3)``

Using these oversold signal together with fundamental analysis, traders will identify and long oversold stocks. Usually, this is during a down trend of a stock due to exacerbate sell-off from negative news. In order to hedge the risk in case the stocks are still going down trend, it is good to know how to hedge major index. 

We can decompose a stock A as a systemic part and a idiocyncratic part. 

``A = \beta Index + \alpha``
