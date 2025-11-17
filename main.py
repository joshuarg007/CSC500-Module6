# Name: Joshua Gutierrez
# Date: November 16 2025
# Description: Main program for online shopping cart

from item_to_purchase import ItemToPurchase
from shopping_cart import ShoppingCart

def print_menu(cart: ShoppingCart):
    choice = ""
    while choice != "q":
        print()
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

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
            # Quit menu loop
            continue

        else:
            # Invalid input, loop will reprint menu
            continue

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()
    print("Customer name:", customer_name)
    print("Today's date:", current_date)

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()