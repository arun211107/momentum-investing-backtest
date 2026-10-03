import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# ==========================================
# SETTINGS
# ==========================================

stocks = [
    "AAPL","MSFT","NVDA","AMZN","GOOGL",
    "META","JPM","V","MA","UNH",
    "HD","PG","XOM","CVX","KO",
    "PEP","MRK","ABBV","COST","WMT",
    "BAC","ORCL","CSCO","NFLX","AMD",
    "IBM","MCD","DIS","CAT","TXN"
]

start_date = "2016-01-01"
end_date = "2025-01-01"

# ==========================================
# DOWNLOAD DATA
# ==========================================

prices = yf.download(
    stocks,
    start=start_date,
    end=end_date,
    auto_adjust=True
)

spy = yf.download(
    "SPY",
    start=start_date,
    end=end_date,
    auto_adjust=True
)

# ==========================================
# PREPARE DATA
# ==========================================

close_prices = prices["Close"]

monthly_prices = close_prices.resample("ME").last()

momentum = monthly_prices.pct_change(12)

# ==========================================
# STRATEGY WITH TRANSACTION COSTS
# ==========================================

transaction_cost = 0.001  # 0.1%

portfolio_returns = []

for i in range(12, len(monthly_prices) - 1):

    current_momentum = momentum.iloc[i].dropna()

    top_stocks = current_momentum.nlargest(
        len(current_momentum) // 3
    ).index

    next_month_returns = (
        monthly_prices.iloc[i + 1][top_stocks]
        / monthly_prices.iloc[i][top_stocks]
        - 1
    )

    portfolio_return = next_month_returns.mean()

    # subtract transaction cost
    portfolio_return = portfolio_return - transaction_cost

    portfolio_returns.append(portfolio_return)

portfolio_returns = pd.Series(
    portfolio_returns,
    index=monthly_prices.index[13:]
)

# ==========================================
# BENCHMARK
# ==========================================

spy_close = spy["Close"]

# If SPY comes back as a DataFrame,
# convert it to a Series
if isinstance(spy_close, pd.DataFrame):
    spy_close = spy_close.iloc[:, 0]

spy_monthly = spy_close.resample("ME").last()

spy_returns = spy_monthly.pct_change()

spy_returns = spy_returns.loc[portfolio_returns.index]

# ==========================================
# CUMULATIVE RETURNS
# ==========================================

strategy_growth = (1 + portfolio_returns).cumprod()

spy_growth = (1 + spy_returns).cumprod()

# ==========================================
# METRICS
# ==========================================

strategy_total_return = float(strategy_growth.iloc[-1] - 1)
spy_total_return = float(spy_growth.iloc[-1] - 1)

years = len(portfolio_returns) / 12

strategy_annual_return = (
    (1 + strategy_total_return) ** (1 / years)
) - 1

spy_annual_return = (
    (1 + spy_total_return) ** (1 / years)
) - 1

strategy_volatility = (
    portfolio_returns.std() * (12 ** 0.5)
)

spy_volatility = (
    spy_returns.std() * (12 ** 0.5)
)

strategy_sharpe = (
    strategy_annual_return /
    strategy_volatility
)

spy_sharpe = (
    spy_annual_return /
    spy_volatility
)

# ==========================================
# MAX DRAWDOWN
# ==========================================

def max_drawdown(series):

    running_peak = series.cummax()

    drawdown = (
        series - running_peak
    ) / running_peak

    return drawdown.min()

strategy_mdd = max_drawdown(strategy_growth)
spy_mdd = max_drawdown(spy_growth)

# ==========================================
# RESULTS
# ==========================================

print("\n===== RESULTS =====\n")

print(f"Strategy Total Return: {strategy_total_return:.2%}")
print(f"SPY Total Return: {spy_total_return:.2%}")

print()

print(f"Strategy Annual Return: {strategy_annual_return:.2%}")
print(f"SPY Annual Return: {spy_annual_return:.2%}")

print()

print(f"Strategy Volatility: {strategy_volatility:.2%}")
print(f"SPY Volatility: {spy_volatility:.2%}")

print()

print(f"Strategy Sharpe Ratio: {strategy_sharpe:.2f}")
print(f"SPY Sharpe Ratio: {spy_sharpe:.2f}")

print()

print(f"Strategy Max Drawdown: {strategy_mdd:.2%}")
print(f"SPY Max Drawdown: {spy_mdd:.2%}")

# ==========================================
# CHART
# ==========================================

plt.figure(figsize=(12, 6))

plt.plot(
    strategy_growth,
    label="Momentum Strategy"
)

plt.plot(
    spy_growth,
    label="SPY Benchmark"
)

plt.title("Momentum Strategy vs S&P 500")
plt.xlabel("Date")
plt.ylabel("Growth of £1")

plt.legend()

plt.savefig("charts/momentum_vs_spy.png", dpi=300)
plt.show()