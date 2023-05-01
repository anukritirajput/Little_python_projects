import os
from art import logo
print(logo)
bids={}
bidding_finished=0
def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        if bidding_record[bidder]>highest_bid:
            highest_bid=bidding_record[bidder]
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while bidding_finished==0:
    name=input("What is  your name?:")
    price=int(input("What is your bid?:$"))
    bids[name]=price
    should_contine=input("Are there other bidders? Type yes or no.\n")

    if should_contine=="no":
        bidding_finished= 1
        find_highest_bidder(bids)
    if should_contine=="yes":
        os.system(
            'cls'
        )
        bidding_finished=0