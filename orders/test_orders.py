import unittest

from orders import amount_due, discount_for


class OrdersTest(unittest.TestCase):
    def test_amount_due_with_tax(self):
        order = {"items": [{"price": "0.00", "qty": 1}, {"price": "10.00", "qty": 2}]}
        self.assertEqual(amount_due(order), 24.20)

    def test_staff_discount_applies_above_threshold(self):
        self.assertEqual(discount_for("STAFF", 200.0), 50.0)

    def test_no_discount_below_threshold(self):
        self.assertEqual(discount_for("STAFF", 50.0), 0.0)


if __name__ == "__main__":
    unittest.main()
