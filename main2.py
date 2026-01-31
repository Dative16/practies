'''3. Supermarket Shopping System
Scenario: A small shop records daily sales.

Task:

Store item names and prices in lists

Calculate total bill

Apply a 10% discount if total > 50,000 Tsh

Print receipt summary'''

products=[]
prices=[]
n=int(input("enter the number of items purchased:"))
for i in range(n):
    product_name=input("enter the name of the product:")
    product_price=input("enter the price of the product:")
    products.append(product_name)
    prices.append(float(product_price))
    total_bill=sum(prices)
    if total_bill>50000:
        discount=total_bill*0.1
        final_bill=total_bill-discount
        print("you have received a discount of:",discount)
        print("final bill after discount:",final_bill)
    else:
        print("no discount applied")
        print("total bill:",total_bill)