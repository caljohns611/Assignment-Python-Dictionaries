#question 1 task 1 

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99},
}

restaurant_menu["Beverages"] = {"Cofee": 4.99, "soda": 2.49}
restaurant_menu["Main Course"]["Steak"] = 17.99
del restaurant_menu["Starters"]["Bruschetta"]


print(restaurant_menu)