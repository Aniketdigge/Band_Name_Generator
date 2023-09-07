#from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

def max_bidding(bid_dictionary):
    max_bid=0
    max_bidder = ""
    for key in bid_dictionary:
        if max_bid<bid_dictionary[key]:
            max_bid = bid_dictionary[key]
            max_bidder = key
    print(f"The winner is {max_bidder} with a bid of ${max_bid}")
    
bidder = {}
user_choise = "yes"

while user_choise=="yes":
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    bidder[name] = bid_amount
    user_choise = input("Are there any other bidders? Type 'yes or 'no'.\n")
    #clear()
        
max_bidding(bidder)




