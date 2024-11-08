#calculating a discount in a project

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        total_price = price-(price*discount_percent/100)
        print("The total price is: ", total_price)
    else:
        print("The total price is: ", price)
# Call the discount calculation function
price = int(input("please enter the price :"))
discount_percent=int(input("Enter the percentage discount: "))
print(calculate_discount(price,discount_percent))     