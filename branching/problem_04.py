# Problem 2:
# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

cost=int(input("what is the cost price of ur product"))
sell=int(input("what is the selling price of ur product"))
if(cost<sell):
    print("You are in profit of, ",sell-cost)
else:
    print("You are in loss of, ",cost-sell)
