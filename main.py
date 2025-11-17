#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: main.py
Author: Joshua R. Gutierrez
Date: November 16, 2025
Version: 1.0
Description: Main program that runs the menu interface for the shopping cart.
"""

from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart


def get_cart_info():
    """Prompt the user for customer name and current date."""
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print()
    print("Customer name:", name)
    print("Today's date:", date)
    return name, date


def show_menu_options():
    """Display the menu options."""
    print()
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")


def print_menu(cart: ShoppingCart):
    """Handle user input for menu operations on the shopping cart."""
    choice = ""

    while choice != "q":
        show_menu_options()
        choice = input("Choose an option:\n")

        if choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = int(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(new_item)

        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            temp_item = ItemToPurchase(item_name=name, item_quantity=quantity)
            cart.modify_item(temp_item)

        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == "q":
            # Quit the menu
            break

        else:
            # Invalid input, loop continues and menu is shown again
            continue


def main():
    """Main entry point for the shopping cart program."""
    customer_name, current_date = get_cart_info()
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
