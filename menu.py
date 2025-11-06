menu={
    'Pizza':50,
    'Pasta':80,
    'Burger':60,
    'Salad':30,
    'Coffee':20,

}
print("Welcome to the restaurant")
print("Pizza: Rs50\nPasta: Rs80\nBurger: Rs60\nSalad: Rs30\nCoffee: Rs20")

order_total = 0

item_1 = input("Enter the first item you want to order:")
if item_1 in menu:
    order_total = order_total + menu[item_1]
    print(f"{item_1} has been added to your order.")
else:
    print(f"Ordered item {item_1} is not available on the menu")

another_order = input("Do you want to add another order? (yes/no):").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} has been added to your order.")
    else:
        print(f"Ordered item {item_2} is not available on the menu")

print(f"The total amount to pay for items in your order is Rs {order_total}")

    