# Binance Futures Testnet Simplified Trading Bot

A Python-based CLI application to interact with the Binance Futures Testnet (USDT-M) [1].

## Features
- **Modular Codebase:** Clean Separation of CLI parsing, input validation, configuration, and trade execution.
- **Order Types Supported:** `MARKET`, `LIMIT`, and `STOP` (Stop-Limit) orders.
- **Robust Error Handling:** Catches validation, networking, and specific exchange API errors safely.
- **Detailed Log Records:** Keeps trace files of every executed order in `bot.log`.

---

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt