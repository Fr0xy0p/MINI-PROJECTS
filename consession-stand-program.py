menu = {"Pizza": 249,
        "Burger": 149,
        "Nachos": 229,
        "Samosa": 49,
        "Coffee": 199,
        "Popcorn": 599}

cart=[]
total = 0
print("- - - - - MENU - - - - -")
for key,value in menu.items():
    print(f"{key:10} : ₹{value:.2f}")
print("- - - - - - - -  - - - -")    

while True:
    food = input("Select an item from Menu(q/Q to quit): ")
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("This item is not avaliable!")  

print("- - - - YOUR CART - - - -")

for food in cart:
    total = total + menu.get(food)
    print(food , end = " , ")

print()
print(f"Your total is: ₹{total}")    
print("Enjoy your Meal sir!")
