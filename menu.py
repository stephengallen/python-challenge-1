menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + " - " + key2)
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2:.2f}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value:.2f}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # Get the customer's input for the item
            item_number = input("Type the item number: ")

            # Check if the customer's input is a number
            if item_number.isdigit():
                # Check if the customer's input is a valid option
                if int(item_number) in menu_items.keys():
                    # Save the item details to a variable
                    selected_item = menu_items[int(item_number)]
                    print(f"You selected {selected_item['Item name']} which costs ${selected_item['Price']:.2f}")

                    # Ask for the quantity
                    quantity = input("How many would you like to order? ")

                    # Check if the quantity is a number
                    if quantity.isdigit():
                        quantity = int(quantity)
                        # Add the selected item to the order list
                        order_list.append({
                            "Item name": selected_item['Item name'],
                            "Price": selected_item['Price'],
                            "Quantity": quantity
                        })
                        print(f"Added {quantity} x {selected_item['Item name']} to your order.")

                    else:
                        print("Invalid quantity. Please enter a number.")

                else:
                    print("Invalid item number. Please select from the list.")

            else:
                print("Invalid input. Please enter a number.")

            # Ask if they want to continue ordering using match statement
            while True:
                response = input("Would you like to order anything else? (y/n) ").lower()

                match response:
                    case 'y':
                        place_order = True
                        break
                    case 'n':
                        place_order = False
                        print("Thank you for your order")
                        break
                    case _:
                        print("Invalid input. Please enter 'y' or 'n'.")

# Print the header of the receipt
print("\nItem name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through the order list and format the receipt
for order in order_list:
    if isinstance(order, dict): 
        item_name = order['Item name']
        price = order['Price']
        quantity = order['Quantity']

        # Calculate the number of spaces needed to align columns
        num_item_spaces = 25 - len(item_name)
        item_spaces = " " * num_item_spaces
        
        # Use string multiplication to create the price and quantity spaces
        price_spaces = " " * (8 - len(f"${price:.2f}"))
        quantity_spaces = " " * (12 - len(str(quantity)))

        # Format and print each line of the receipt
        print(f"{item_name}{item_spaces} | ${price:.2f}{price_spaces} | {quantity}{quantity_spaces}")

# Calculate the total price using list comprehension and sum()
total_price = sum([order['Price'] * order['Quantity'] for order in order_list])

# Print the total price
print(f"\nTotal price: ${total_price:.2f}")
print("Thank you for your business! Please come again soon!")