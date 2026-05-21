# Binance Futures Testnet Simplified Trading Bot

A Python-based CLI application to interact with the Binance Futures Testnet (USDT-M).

---

## ✨ Features

- **Modular Codebase:** Clean separation of CLI parsing (`cli.py`), input validation (`validators.py`), configuration, and trade execution (`orders.py`).
- **Defensive Design:** Uses safe dictionary `.get()` lookups to handle nested API outputs without runtime crashes.
- **Order Types Supported:** `MARKET`, `LIMIT`, and `STOP` (Stop-Limit) — completed as a bonus feature.
- **Robust Observability:** Complete exception handling and structured logging to both standard output and a persistent file (`bot.log`).

---

## 📁 Project Structure

```
Trading Bot - Binance/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
├── .env
├── .gitignore
├── bot.log
├── cli.py
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🚀 Setup & Execution

### Prerequisites

- Python 3.8+
- A Binance Futures Testnet account with API credentials

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd trading-bot-binance
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
API_KEY=your_binance_futures_testnet_api_key
SECRET_KEY=your_binance_futures_testnet_secret_key
```

---

## 📖 Usage Examples

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 78000
```

### Stop-Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.01 --price 79500 --stop-price 79000
```

---

## 📝 Assumptions & Design Choices

- **USDT-M Futures Only:** The bot targets the USDT-M Futures Testnet exchange via the `futures_create_order` API method, and enforces validation checks that all symbols end with `USDT`.
- **Defensive Error Handling:** Standardized error formats are used across all modules to gracefully handle invalid price filters, missing credentials, and network dropouts.