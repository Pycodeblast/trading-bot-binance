import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging


def extract_avg_price(order):
    """
    Extract average price from order response.
    Works for both LIMIT and MARKET orders.
    """
    avg_price = order.get("avgPrice")

    # For MARKET orders (Spot), price may be inside 'fills'
    if not avg_price and "fills" in order:
        fills = order.get("fills", [])
        if fills:
            avg_price = fills[0].get("price")

    return avg_price or "N/A"


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    # Normalize input
    args.symbol = args.symbol.upper()
    args.side = args.side.upper()
    args.type = args.type.upper()

    try:
        # Validate input
        validate_input(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        client = get_client()

        # Print request summary
        print("\nOrder Request:")
        print({
            "symbol": args.symbol,
            "side": args.side,
            "type": args.type,
            "quantity": args.quantity,
            "price": args.price
        })

        # Place order
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        if order:
            avg_price = extract_avg_price(order)

            print("\nOrder Success:")
            print({
                "orderId": order.get("orderId"),
                "status": order.get("status"),
                "executedQty": order.get("executedQty"),
                "avgPrice": avg_price
            })
        else:
            print("\nOrder Failed")

    except ValueError as ve:
        print(f"\nValidation Error: {str(ve)}")

    except Exception as e:
        print(f"\nUnexpected Error: {str(e)}")


if __name__ == "__main__":
    main()