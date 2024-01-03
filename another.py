#Delima, Sheena Mae D.
#BSCPE1-5


#-----------------------------------------------


# ========= FUNCTIONS =========
def asking_the_user(dessert_type):
    return int(input("Please Enter the Total Number of " + dessert_type + " you want to buy: "))

def computation_of_the_money(type_of_dessert, dessert_price):
    return type_of_dessert * dessert_price


# ========= ACTUAL CODES =========
# --- Pseudocode --
# - Asking the user the total number of a certain dessert she/he wants
ice_cream_dessert = asking_the_user("ice cream")
yogurt_dessert = asking_the_user("yogurt")

# - User's money in his/her pocket
user_money = 5000

# - Price of the Desserts
ice_cream_price = 150
yogurt_price = 100

# - Product of each dessert
product_of_ice_cream_dessert = computation_of_the_money(ice_cream_dessert, ice_cream_price)
print("The total product if we multiply the user's desired total number of ice  cream and price is: " + str(product_of_ice_cream_dessert))# The line `product_of_yogurt_dessert = computation_of_the_money(yogurt_dessert, yogurt_price)` is calling the `computation_of_the_money` function and passing the `yogurt_dessert` and `yogurt_price` as arguments. This function will then multiply the number of yogurt desserts the user wants to buy (`yogurt_dessert`) by the price of each yogurt dessert (`yogurt_price`). The result will be assigned to the variable `product_of_yogurt_dessert`.
product_of_yogurt_dessert = computation_of_the_money(yogurt_dessert, yogurt_price)
print("The total product if we multiply the user's desired total number of yogurt and price is: " + str(product_of_yogurt_dessert))

# - Total amount the user spend
total_amount = product_of_ice_cream_dessert + product_of_yogurt_dessert
print("The total amount of the user she spend is: " + str(total_amount))

# - Change of the user
print("The total change does user the have is: " + str(user_money - total_amount))

# Note: Use a "define" function when executing this task



