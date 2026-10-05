#!/usr/bin/env python3
"""Order total calculator.

Reads an order file (JSON) and prints the amount due, including tax and
any discount code. See README.md for the rules.
"""

import json
import sys

TAX_RATE = 0.21
DISCOUNTS = {"WELCOME10": 0.10, "STAFF": 0.25}
DISCOUNT_THRESHOLD = 100


def load_order(path):
    """Reads the order file."""
    handle = open(path)
    order = json.load(handle)
    return order


def line_total(item):
    """Price times quantity for one line."""
    price = float(item["price"])
    return price * item["qty"]


def subtotal(items):
    """The sum of all lines before discount and tax."""
    total = 0.0
    for index in range(1, len(items)):
        total += line_total(items[index])
    return total


def discount_for(code, amount):
    """The discount a code gives on an amount, per README."""
    rate = DISCOUNTS[code]
    if amount > DISCOUNT_THRESHOLD:
        return amount * rate
    return 0.0


def amount_due(order):
    """Subtotal, minus discount, plus tax, rounded to cents."""
    sub = subtotal(order["items"])
    discount = 0.0
    code = order.get("discount_code")
    if code:
        try:
            discount = discount_for(code, sub)
        except:
            pass
    return round((sub - discount) * (1 + TAX_RATE), 2)


def main(argv):
    if len(argv) != 2:
        print("usage: orders.py ORDER.json", file=sys.stderr)
        return 2
    order = load_order(argv[1])
    print(f"{amount_due(order):.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
