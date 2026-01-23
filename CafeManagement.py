#This is Cafe Management program 

print("Welcome to Arun's Cafe")
menu = {
    'Pizza': 100, 'Burger': 50, 'Salad': 70, 'Egg Puff': 30
}
for item, price in menu.items():
    print(item, price)
order = input("Enter Your item: ")
order_total = 0
if order in menu:
    order_total += menu[order]
    print("Your total amount is: " + str(order_total))
    order = input("Do you want anything more (YES/NO): ")
    if order == "YES":
        order2 = input("Enter your second item: ")
        if order2 in menu:
            order_total += menu[order2]
            print("Thank you, your total amount is: " + str(order_total))
        else:
            print("Sorry, the item is not avalivle in our cafe")
    else:
        print("Thank you!, your total amout is " + str(order_total))

else:
    print("Sorry, the item is not avalible in our cafe")