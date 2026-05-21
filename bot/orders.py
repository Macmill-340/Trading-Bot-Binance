from binance.exceptions import BinanceAPIException
from bot.logging_config import setup_logging
from bot.validators import validate_symbol, validate_order_params

logger = setup_logging()

def place_order(client, symbol: str, side: str, order_type: str, quantity: float, price: float=None, stop_price: float=None):
    try:
        symbol = validate_symbol(symbol)
        side = side.upper()
        order_type_upper = order_type.upper()
        validate_order_params(order_type_upper, quantity, price, stop_price)
    except ValueError as val_err:
        logger.error(f"Validation Error: {str(val_err)}")
        return False, str(val_err)

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type_upper,
        "quantity": quantity,
    }

    if order_type_upper == "LIMIT":
        params["price"] = str(price)
        params["timeInForce"] = "GTC"
    elif order_type_upper == "STOP":
        params["price"] = str(price)
        params["stopPrice"] = str(stop_price)
        params["timeInForce"] = "GTC"

    logger.info(f"Sending Order Request Summary: {params}")

    try:
        #create order
        response = client.futures_create_order(**params)
        logger.info(f"API Response received successfully: {response}")

        summary = {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A"),
        }
        return True, summary

    except BinanceAPIException as e:
        error_msg = f"Binance API Error: {e.message} Code: {e.code}"
        logger.error(error_msg)
        return False, error_msg
    except Exception as e:
        error_msg = f"Unexpected system error: {str(e)}"
        logger.error(error_msg)
        return False, error_msg