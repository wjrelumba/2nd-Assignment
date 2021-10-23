money = int(input("Enter the amount of money you have:"))
apple_pr = int(input("Enter the price of apple:"))
amo_apple = money // apple_pr
change = money % apple_pr
print(f"You can buy {amo_apple} apples and your change is {change} pesos.")