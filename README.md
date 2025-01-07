# Backtest-SMA-Crossover-Strategy

This repository provides a framework for **backtesting and optimizing trading strategies** using Python. The primary focus is a **Simple Moving Average (SMA) Crossover Strategy**, implemented with the help of the **Backtesting.py** library. The strategy is designed to test the performance of different moving average combinations on stock data fetched via **Yahoo Finance (yfinance)**.

## Features

- **SMA Crossover Strategy**: Implements a simple crossover approach to generate buy/sell signals based on short-term and long-term moving averages.
- **Backtesting Framework**: Uses **Backtesting.py** to simulate and analyze historical performance.
- **Optimization Support**: Includes parameter optimization for SMA periods to maximize returns.
- **Yahoo Finance Data Integration**: Fetches historical stock data directly from **yfinance**.
- **Performance Metrics**: Evaluates key statistics like returns, Sharpe ratio, and drawdowns.

## Dependencies

The project requires the following Python libraries:

- `backtesting` - For strategy simulation and analysis
- `yfinance` - For downloading historical stock data
- `pandas` - For data manipulation and formatting
- `numpy` - For numerical computations

Install the dependencies with:
```bash
pip install backtesting yfinance pandas numpy
```

## How It Works

1. **SMA Strategy Definition**:
   - Two moving averages (short-term and long-term) are calculated.
   - Buy signals are generated when the shorter SMA crosses above the longer SMA.
   - Sell signals are generated when the shorter SMA crosses below the longer SMA.

2. **Backtest Execution**:
   - Historical stock data is fetched using **yfinance**.
   - The strategy is simulated using **Backtesting.py** with customizable parameters such as initial cash and commission rates.

3. **Optimization**:
   - The SMA periods are optimized to find the best-performing combination based on return percentage.

## Usage

Run the main script to execute the backtest and optimization:
```bash
python main.py
```

### Example Output:
```
Start                     2024-01-01
End                       2024-12-31
Duration                  365 days 00:00:00
Exposure Time [%]         85.2
Equity Final [$]          150000
Return [%]                50.0
Sharpe Ratio              1.35
```

## File Structure

- **main.py**: Core script implementing the SMA Crossover strategy and backtesting pipeline.
- **requirements.txt**: List of required dependencies.
- **README.md**: Documentation for the project.

## Customization

- **Parameters**: Adjust SMA periods (`n1` and `n2`) in the strategy class to experiment with different combinations.
- **Data Source**: Replace the ticker symbol (e.g., `SILK.KA`) with your preferred stock symbol.
- **Timeframe**: Modify the date range to test performance over different periods.

## Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, and create pull requests for enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

