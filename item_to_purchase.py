#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: item_to_purchase.py
Author: Joshua R. Gutierrez
Date: November 16, 2025
Version: 1.0
Description: Class representing an item that can be added to a shopping cart.
"""

class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")
