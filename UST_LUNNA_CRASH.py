# pip install yfinance pandas matplotlib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1️⃣ Get LUNA Classic prices
# -----------------------------
luna = yf.Ticker('LUNC-USD')
luna_data = luna.history(
    start='2021-01-01',
    end='2022-06-01',
    interval='1d'
)

# -----------------------------
# 2️⃣ Get UST prices daily
# -----------------------------
ust = yf.Ticker('UST-USD')
ust_data = ust.history(
    start='2021-01-01',
    end='2022-06-01',
    interval='1d'
)

# -----------------------------
# 3️⃣ Plot both price trends
# -----------------------------
plt.figure(figsize=(14, 7))

plt.plot(luna_data.index, luna_data['Close'], label='LUNA (Classic)', color='crimson')
plt.plot(ust_data.index, ust_data['Close'], label='UST (Stablecoin)', color='gold')

plt.title('Terra LUNA & UST Collapse (2021–2022)', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# 4️⃣ Estimate LUNA cap loss
# -----------------------------

# Peak price LUNA
luna_peak_price = luna_data['Close'].max()

# Final price LUNA
luna_final_price = luna_data['Close'].iloc[-1]

# Peak supply estimate
luna_peak_supply = 350_000_000  # ~350 million LUNA

initial_mcap = luna_peak_price * luna_peak_supply
final_mcap = luna_final_price * luna_peak_supply

loss = initial_mcap - final_mcap

print(f"🔴 Peak LUNA price: ${luna_peak_price:.2f}")
print(f"🔵 Final LUNA price: ${luna_final_price:.8f}")
print(f"💥 Estimated market cap wiped out: ${loss/1e9:.2f} billion USD (approx)")
