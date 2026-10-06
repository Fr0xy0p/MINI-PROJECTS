Foods = []
Prices = []
total = 0

while True:
    food = input("Enter a food to buy (q/Q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter thr price of the {food}: ₹" ))
        Foods.append(food)
        Prices.append(price)

print("_____YOUR CART_____")

for food in Foods:
    print(food)
for price in Prices:
    total += price

print(f"Your total is :₹ {total}")
