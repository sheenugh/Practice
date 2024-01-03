#Delima, Sheena Mae D.
#BSCPE1-5


#-----------------------------------------------


# ========= FUNCTIONS =========
def asking_the_user(dessert_type):
    return int(input("Please Enter the Total Number of " + dessert_type + " you want to buy: "))

def computation_of_the_money(type_of_dessert, dessert_price):
    return type_of_dessert * dessert_price

# ========= IMPORT =========


# ========= ACTUAL CODES =========
# --- Pseudocode --
# - Variable for the dessert type and for the def function + print function
ice_cream_dessert = asking_the_user("ice cream")
yogurt_dessert = asking_the_user("yogurt")

# - User's money in his/her pocket
user_money = 5000

# - Price of the Desserts
ice_cream_price = 150
yogurt_price = 100

# - Multiplying each of the dessert from the user's desired total she/he picked by its constant price
product_of_ice_cream_dessert = (ice_cream_dessert * ice_cream_price)
print("The total product if we multiply the user's desired total number of ice  cream and price is: " + str(product_of_ice_cream_dessert))
product_of_yogurt_dessert = (yogurt_dessert * yogurt_price)
print("The total product if we multiply the user's desired total number of yogurt and price is: " + str(product_of_yogurt_dessert))

# - Total amount the user spend

# Note: Use a "define" function when executing this task
# Total amount of change




