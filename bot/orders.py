import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        # Log request clearly
        logging.info(
            f"REQUEST → symbol={symbol}, side={side}, type={order_type}, quantity={quantity}, price={price}"
        )

        # MARKET ORDER
        if order_type == "MARKET":
            order = client.create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        # LIMIT ORDER
        elif order_type == "LIMIT":
            order = client.create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=str(price),  # Binance expects string sometimes
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        # Log response
        logging.info(f"RESPONSE → {order}")

        return order

    except Exception as e:
        # Log error
        logging.error(f"ERROR → {str(e)}")
        return None