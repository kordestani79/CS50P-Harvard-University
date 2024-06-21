# Define the menu
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Function to calculate total cost
def calculate_total(items):
    total = 0
    for item in items:
        if item in menu:
            total += menu[item]
    return total

# Function to prompt user for order
def place_order():
    items = []
    print("Welcome to Felipe's Taqueria!")
    print("Please enter your order one item at a time. Press Ctrl-D when finished.")
    try:
        while True:
            item = input().strip().title()
            items.append(item)
            total = calculate_total(items)
            print(f"Total: ${total:.2f}")
    except EOFError:
        pass
    finally:
        return items

# Main function
def main():
    items = place_order()
    total = calculate_total(items)
    print(f"Your total is: ${total:.2f}")

if __name__ == "__main__":
    main()
