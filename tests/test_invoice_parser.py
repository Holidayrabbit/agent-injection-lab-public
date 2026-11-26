import unittest

from invoice_parser import parse_amount


class InvoiceParserTests(unittest.TestCase):
    def test_whole_amount(self):
        self.assertEqual(parse_amount("Total: 42 USD"), 4200)

    def test_fractional_amount(self):
        self.assertEqual(parse_amount("Total: 42.7 USD"), 4270)

