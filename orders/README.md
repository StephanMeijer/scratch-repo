# orders

A small command line tool that prints the amount due for an order.

    python3 orders.py order.json

The order file is JSON:

    {
      "items": [{"price": "19.99", "qty": 2}, {"price": "5.00", "qty": 1}],
      "discount_code": "WELCOME10"
    }

Rules:

- Prices are in euros with two decimals; the amount due is rounded to cents.
- Tax is 21 percent, applied after the discount.
- Orders with a subtotal of 100.00 or more qualify for a discount code.
- An unknown discount code is an error and the order is not priced.

Run the tests with `python3 -m unittest` from this directory.
