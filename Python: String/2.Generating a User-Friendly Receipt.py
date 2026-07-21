# Generating a User-Friendly Receipt

# Use : string formatting

# Problem : Store the formatted receipt in a variable called formatted_receipt and print it.

#Solution

def generate_receipt(item1, price1, item2, price2, item3, price3):
    Total_price = price1 + price2 + price3

    formatted_receipt = f"""Item Price
{item1} ${price1:.2f}
{item2} ${price2:.2f}
{item3} ${price3:.2f}
Total ${Total_price:.2f}
    """

    print(formatted_receipt)

