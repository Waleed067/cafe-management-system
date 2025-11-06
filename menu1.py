# Improved Basic Restaurant Menu Program

menu = {
    'pizza': 50,
    'pasta': 80,
    'burger': 60,
    'salad': 30,
    'coffee': 20,
    'tea': 15,
    'sandwich': 40,
}

print("🍽️ Welcome to the Restaurant!")
print("\n--- MENU ---")
for item, price in menu.items():
    print(f"{item.capitalize()}: Rs{price}")

order_total = 0
ordered_items = []

while True:
    item = input("\nEnter the item you want to order: ").strip().lower()

    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)
        print(f"✅ {item.capitalize()} has been added to your order.")
    else:
        print(f"❌ Sorry, {item.capitalize()} is not available on the menu.")

    another = input("Do you want to order another item? (yes/no): ").strip().lower()
    if another != 'yes':
        break

# Display Bill
print("\n🧾 --- Your Order Summary ---")
for item in ordered_items:
    print(f"{item.capitalize()} - Rs{menu[item]}")
print("---------------------------")
print(f"Total Amount to Pay: Rs {order_total}")
print("Thank you for visiting! 😊")
