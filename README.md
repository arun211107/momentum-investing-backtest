# Momentum Investing Strategy Backtest

## Overview

This project investigates whether a simple momentum investing strategy could have outperformed the market over the period 2016–2025.

Momentum investing is based on the idea that stocks which have performed strongly in the recent past may continue to perform well in the future. To test this hypothesis, I built a systematic backtest in Python using historical stock market data.

The strategy was compared against a passive investment in the S&P 500 through the SPY ETF, and performance was evaluated using both return and risk metrics.

---

## Research Question

Can a simple momentum investing strategy outperform a passive market benchmark over the long term?

---

## Methodology

### Investment Universe

The strategy uses a universe of 30 large-cap US stocks:

- AAPL
- MSFT
- NVDA
- AMZN
- GOOGL
- META
- JPM
- V
- MA
- UNH
- HD
- PG
- XOM
- CVX
- KO
- PEP
- MRK
- ABBV
- COST
- WMT
- BAC
- ORCL
- CSCO
- NFLX
- AMD
- IBM
- MCD
- DIS
- CAT
- TXN

### Benchmark

- SPY (S&P 500 ETF)

### Strategy Rules

1. Download monthly stock prices from Yahoo Finance.
2. Calculate each stock's return over the previous 12 months.
3. Rank all stocks by this 12-month return.
4. Select the top third of performers.
5. Invest equally across the selected stocks.
6. Hold for one month.
7. Rebalance monthly and repeat throughout the sample period.
8. Apply a transaction cost of 0.1% at each rebalance.

To avoid look-ahead bias, portfolio decisions are made using only information available prior to each investment period.

---

## Technologies Used

- Python
- pandas
- NumPy
- matplotlib
- yfinance

---

## Results

| Metric | Momentum Strategy | SPY Benchmark |
|----------|----------:|----------:|
| Total Return | 410.93% | 194.08% |
| Annualised Return | 22.88% | 14.60% |
| Volatility | 18.82% | 16.17% |
| Sharpe Ratio | 1.22 | 0.90 |
| Maximum Drawdown | -20.34% | -23.93% |

---

## Visualisation

The chart below compares the growth of £1 invested in the momentum strategy against £1 invested in the S&P 500 benchmark.

<img width="1200" height="600" alt="Momentum strat vs SPY 2" src="https://github.com/user-attachments/assets/2a5e6cc4-d72a-4853-a884-f4b453541642" />

---

## Interpretation

The momentum strategy substantially outperformed the benchmark over the sample period.

While the strategy experienced slightly higher volatility, it generated significantly higher returns and achieved a higher Sharpe Ratio, indicating stronger risk-adjusted performance. The strategy also experienced a smaller maximum drawdown than the benchmark.

These results are broadly consistent with the momentum effect documented in academic finance literature.

---

## Limitations

This project has several limitations:

- Survivorship bias: the stock universe consists of companies that are large and successful today.
- Limited sample period: results may differ across different market environments.
- Simplified transaction cost assumptions.
- No consideration of taxes, bid-ask spreads, or market impact.
- Past performance does not guarantee future returns.

---

## Key Takeaways

- Built a systematic investment strategy using Python.
- Worked with real-world financial market data.
- Implemented a historical backtest.
- Evaluated both return and risk metrics.
- Explored a practical application of the Efficient Market Hypothesis and factor investing.

---

## Disclaimer

This project was created for educational purposes only and should not be considered investment advice.
