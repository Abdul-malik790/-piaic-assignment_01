# The price of one note book is 80 rupees
# if you buy 7 notebooks.calculate the total price
# if you have 600 rupees,check(using comparsion operator)weather your money is enough to buy them or not 
# print the result in a clear message 

# Solution

notebook_price = 80
quantity = 7
money_available = 600
# Calculate total cost
total_cost = notebook_price * quantity
# Check if the money is enough
is_enough = money_available >= total_cost
# Print results
print("Total cost of 7 notebooks:", total_cost, "rupees")
