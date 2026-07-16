# Discount Calculation Based on Membership and Spending

# Difficulty : Medium
# use : lambda function

# solution

def apply_discount(total_amount, membership_level):
    
    discount_calculation = lambda x : (
                            .05 if x == "silver"
                            else .10 if x == "gold"
                            else .15
    )

    discount_rate = discount_calculation(membership_level)

    if total_amount > 1000:
        amount = total_amount - (total_amount * discount_rate) - (total_amount * .15)
    elif total_amount <= 1000 or total_amount > 500:
        amount = total_amount - (total_amount * discount_rate) - (total_amount * .05)
    else:
        amount = total_amount - (total_amount * discount_rate)

    return amount
