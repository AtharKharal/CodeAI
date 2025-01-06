from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import yfinance as yf



class SmaCross(Strategy):
    # Define the two MA lags as *class variables*
    # for later optimization
    n1 = 25
    n2 = 30
    
    def init(self):
        # Precompute the two moving averages
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
    
    def next(self):
        # If sma1 crosses above sma2, close any existing
        # short trades, and buy the asset
        if crossover(self.sma1, self.sma2):
            self.position.close()
            self.buy()

        # Else, if sma1 crosses below sma2, close any existing
        # long trades, and sell the asset
        elif crossover(self.sma2, self.sma1):
            self.position.close()
            self.sell()

# Download stock data
data = yf.download("SILK.KA", start="2024-01-01", end="2024-12-31")
data.columns = data.columns.droplevel(1)
data.columns.name = None
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
data.index.name=None
print(data)


# Run the backtest
bt = Backtest(data, SmaCross, cash=100000, commission=0.002)

# Optimize the strategy
stats = bt.optimize(n1=range(5, 30, 5),
                    n2=range(10, 70, 10),
                    maximize='Return [%]',
                    constraint=lambda p: p.n1 < p.n2)

print(stats)

# Display full optimization results
print(stats._strategy)



# # =======================
# stats = bt.run()
# print(stats)
# # btOptimized = bt.optimize(n1=range(5, 30, 5), n2=range(30, 60, 5))

# optimized_results = bt.optimize(n1=range(5, 30, 5), n2=range(30, 60, 5),
#                                 method='skopt', 
#                                 return_optimization=True)

# # Access optimized parameters
# n1_opt, n2_opt = optimized_results[0], optimized_results[1]

# # Access fitness and score
# # fitness = optimized_results[0]["fitness"]
# # score = optimized_results[1]["score"]

# print(f"Optimized parameters: n1={n1_opt}, n2={n2_opt}")
# print(f"Fitness: {fitness}")
# print(f"Score: {score}")
