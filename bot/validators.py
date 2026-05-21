def validate_symbol(symbol: str) -> str:
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string.")

    symbol_upper = symbol.strip().upper()
    if not symbol_upper.endswith('USDT'):
        raise ValueError("Only USDT-M futures pairs (e.g., BTCUSDT) are currently supported.")
    return symbol_upper

def validate_order_params(order_type: str, quantity: float, price: float = None, stop_price: float = None):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    order_type_upper = order_type.upper()

    if order_type_upper == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("Price must be greater than zero for LIMIT orders.")

    elif order_type_upper == "STOP":
        if price is None or price <= 0:
            raise ValueError("Price must be greater than zero for STOP orders.")
        if stop_price is None or stop_price <= 0:
            raise ValueError("Stop price must be greater than zero for STOP orders.")
