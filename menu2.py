# Intermediate Restaurant Billing System 🧾

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
    print(f"{item.capitalize():<10} Rs{price}")

order_total = 0
order_details = []

while True:
    item = input("\nEnter the item you want to order: ").strip().lower()

    if item in menu:
        quantity = int(input(f"Enter quantity for {item.capitalize()}: "))
        item_total = menu[item] * quantity
        order_total += item_total
        order_details.append((item, quantity, menu[item], item_total))
        print(f"✅ Added {quantity} x {item.capitalize()} to your order.")
    else:
        print(f"❌ Sorry, {item.capitalize()} is not available.")

    another = input("Do you want to order another item? (yes/no): ").strip().lower()
    if another != 'yes':
        break

# --- Apply Discount and Tax ---
discount = 0
if order_total > 200:
    discount = 0.1 * order_total  # 10% discount

tax = 0.05 * order_total  # 5% tax
final_total = order_total - discount + tax

# --- Print Bill ---
print("\n🧾 --- BILL SUMMARY ---")
print(f"{'Item':<12}{'Qty':<6}{'Price':<8}{'Total'}")
print("-" * 35)
for item, qty, price, total in order_details:
    print(f"{item.capitalize():<12}{qty:<6}{price:<8}{total}")
print("-" * 35)
print(f"{'Subtotal':<25}Rs {order_total}")
print(f"{'Discount (10%)':<25}-Rs {discount:.2f}")
print(f"{'Tax (5%)':<25}+Rs {tax:.2f}")
print("=" * 35)
print(f"{'Grand Total':<25}Rs {final_total:.2f}")
print("\nThank you for visiting! 😊")
