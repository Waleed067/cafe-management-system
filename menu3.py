import datetime

# 🍽️ Menu Dictionary
menu = {
    'pizza': 50,
    'pasta': 80,
    'burger': 60,
    'salad': 30,
    'coffee': 20,
    'tea': 15,
    'sandwich': 40,
}

# 📜 Function to display the menu
def show_menu():
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item.capitalize():<10} Rs {price}")

# 🧮 Function to take the order
def take_order():
    order_total = 0
    order_details = []

    while True:
        item = input("\nEnter the item you want to order: ").strip().lower()

        if item in menu:
            # Safe quantity input
            try:
                quantity = int(input(f"Enter quantity for {item.capitalize()}: "))
                if quantity <= 0:
                    print("❌ Quantity must be positive.")
                    continue
            except ValueError:
                print("❌ Please enter a valid number for quantity.")
                continue

            item_total = menu[item] * quantity
            order_total += item_total
            order_details.append((item, quantity, menu[item], item_total))
            print(f"✅ Added {quantity} x {item.capitalize()} to your order.")
        else:
            print(f"❌ Sorry, {item.capitalize()} is not available on the menu.")

        another = input("Do you want to order another item? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    return order_details, order_total

# 💾 Function to save bill to a text file
def save_bill(order_details, order_total, discount, tax, final_total):
    now = datetime.datetime.now()
    file_name = f"bill_{now.strftime('%Y%m%d_%H%M%S')}.txt"

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("🧾 RESTAURANT BILL RECEIPT\n")
        file.write(f"Date: {now.strftime('%d-%m-%Y %H:%M:%S')}\n")
        file.write("-" * 40 + "\n")
        file.write(f"{'Item':<12}{'Qty':<6}{'Price':<8}{'Total'}\n")
        file.write("-" * 40 + "\n")
        for item, qty, price, total in order_details:
            file.write(f"{item.capitalize():<12}{qty:<6}{price:<8}{total}\n")
        file.write("-" * 40 + "\n")
        file.write(f"{'Subtotal':<25}Rs {order_total:.2f}\n")
        file.write(f"{'Discount (10%)':<25}-Rs {discount:.2f}\n")
        file.write(f"{'Tax (5%)':<25}+Rs {tax:.2f}\n")
        file.write("=" * 40 + "\n")
        file.write(f"{'Grand Total':<25}Rs {final_total:.2f}\n")
        file.write("-" * 40 + "\n")
        file.write("Thank you for visiting! 😊\n")

    print(f"\n🧾 Bill saved successfully as '{file_name}'")

# 🏁 Main Program
print("🍽️ Welcome to the Restaurant!")
show_menu()

# Take orders
order_details, order_total = take_order()

# Apply discount & tax
discount = 0
if order_total > 200:
    discount = 0.1 * order_total  # 10% discount
tax = 0.05 * order_total
final_total = round(order_total - discount + tax, 2)

# Display Bill Summary
print("\n🧾 --- BILL SUMMARY ---")
print(f"{'Item':<12}{'Qty':<6}{'Price':<8}{'Total'}")
print("-" * 35)
for item, qty, price, total in order_details:
    print(f"{item.capitalize():<12}{qty:<6}{price:<8}{total}")
print("-" * 35)
print(f"{'Subtotal':<25}Rs {order_total:.2f}")
print(f"{'Discount (10%)':<25}-Rs {discount:.2f}")
print(f"{'Tax (5%)':<25}+Rs {tax:.2f}")
print("=" * 35)
print(f"{'Grand Total':<25}Rs {final_total:.2f}")
print("\nThank you for visiting! 😊")

# Ask before saving the bill
save = input("\nDo you want to save this bill? (yes/no): ").strip().lower()
if save == "yes":
    save_bill(order_details, order_total, discount, tax, final_total)
else:
    print("🗑️ Bill not saved. Have a nice day!")
