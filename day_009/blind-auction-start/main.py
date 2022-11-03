from replit import clear
#HINT: You can call clear() to clear the output in the console.
# Import logo and print
from art import logo
print(logo)
print("Welcome to the secret auction program!")
auction = {}
auction_continue = True
while auction_continue == True:
    # Ask for name input
    name = input("What is your name?: ")
    # Ask for bid price
    bid = int(input("What's your bid?: "))
    
    #add bid to Auction dictionary
    
    auction.update({name: bid})
    
    ####
    # Testing code
    # for key in auction:
    #     print(name)
    #     print(auction[key])
    #print(auction[name,bid)
    ####
    
    continue_bidding = input("Are there any other bidders? type 'yes' or 'no'. ").lower()
    if continue_bidding == "yes":
        auction_continue = True
        clear()
    elif continue_bidding == "no":
        auction_continue = False
        print("Auction done")
# To find max value in dictionary max() and dict.get() method       
bids = auction.values()
highest_bid = max(bids)
# To find the name of highest bidder search dictionary by value using dictionary comprehension in for loop
new_val = highest_bid
highest_bidder=[new_k for new_k in auction.items() if new_k[1] == new_val][0][0]
# Testing code
# for key in auction:
#     #print(name)
#     print(auction[key])
#     #print(auction)
print(f"The winner is {highest_bidder} with a bid of £{highest_bid}.")
