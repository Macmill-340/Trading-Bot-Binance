import argparse
from bot.client import get_client
from bot.orders import place_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot CLI Interface")

    parser.add_argument("--symbol", type=str, required=True, help="e.g., BTCUSDT")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL"], help="BUY or SELL")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT", "STOP"],
                        help="MARKET, LIMIT, or STOP")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, required=False, help="Required for LIMIT and STOP orders")
    parser.add_argument("--stop-price", type=float, required=False, help="Required trigger price for STOP orders")

    args = parser.parse_args()

    #check to prevent unnecessary calls
    if args.type.upper() in ["LIMIT", "STOP"] and args.price is None:
        parser.error(f"--price is required when --type is {args.type.upper()}.")
    if args.type.upper() == "STOP" and args.stop_price is None:
        parser.error("--stop-price is required when --type is STOP.")

    print("\n--- Initiating Order Request ---")
    try:
        client = get_client()
        success, result = place_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
            stop_price=args.stop_price
        )

        if success:
            print("\n✅ ORDER SUCCESSFUL")
            print(f"Order ID: {result.get('orderId', 'N/A')}")
            print(f"Status: {result.get('status', 'N/A')}")
            print(f"Executed Qty: {result.get('executedQty', 'N/A')}")
            print(f"Avg Price: {result.get('avgPrice', 'N/A')}")
        else:
            print(f"\n❌ ORDER FAILED\nDetails: {result}")

    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {e}")


if __name__ == "__main__":
    main()