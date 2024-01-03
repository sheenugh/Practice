#pseudocode


# -- IMPORTS ---


# --- FUNCTIONS ---
def ask_user_to_input_a_number(fruit_type):
    return int(input("Please input a number of " + fruit_type + " you want to buy: "))

def computation_of_the_total_amount_of_the_fruits(type_of_fruit, fruit_price):
    return type_of_fruit * fruit_price

# --- ACTUAL CODES ---
# - Ask user for the total number of apples he/she wants to buy
apple_type = ask_user_to_input_a_number("apples")

# - Ask user for the total number of oranges he/she wants to buy
orange_type = ask_user_to_input_a_number("oranges")

# - Price
apples_price = 20
orange_price = 30 

# - Computation
total_amount_of_apple = computation_of_the_total_amount_of_the_fruits(apple_type, apples_price)
total_amount_of_orange = computation_of_the_total_amount_of_the_fruits(orange_type, orange_price)
overall_amount = total_amount_of_apple + total_amount_of_orange

# - Displaying the output
print("The total amount that the user bought is " + str(overall_amount))

