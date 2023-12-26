from replit import clear
#HINT: You can call clear() to clear the output in the console.

########## Function definitions.

def get_name(n_prompt):
  correct = True
  name = input(n_prompt)
  if(not name.isalpha()):
    correct = False
    while not correct:
      print("Please enter a valid name.")
      name = input(n_prompt)
      if name.isalpha():
        correct = True
  return name

def get_bid(b_prompt):
  correct = True
  bid = input(b_prompt)
  if not bid.isnumeric() or int(bid) <= 0:
    correct = False
    while not correct:
      print("Please enter a valid bid.")
      bid = input(b_prompt)
      if bid.isnumeric() and int(bid) > 0:
        correct = True
  return bid
  
def add_to_dictionary(dictionary):
  name_prompt = "Name: "
  name = get_name(name_prompt)
  bid_prompt = "Bid: $"
  bid = get_bid(bid_prompt)
  dictionary[name] = bid

def remaining_bidders(prompt):
  correct = True
  still_going = input(prompt).lower()
  if still_going != "yes" and still_going != "no":
    correct = False
    while not correct:
      print("Please type a viable option.")
      still_going = input(prompt).lower()
      if still_going == "yes" or still_going == "no":
        correct = True
  return still_going


def determine_winner(dictionary):
  name = list(dictionary.keys())[0]
  max = list(dictionary.values())[0]
  for i in dictionary:
    if dictionary[i] > max:
      name = i
      max = dictionary[i]
  clear()
  print(f"The winner is {name} with a bid of ${max}.")
  
########## Functions defined.

import art

print(art.logo)
print("Welcome to the Secret Auction")

bidders = {}
add_to_dictionary(bidders)
more_bidders_prompt = "Are there other bidders? 'yes' or 'no': "
if (more_bidders := remaining_bidders(more_bidders_prompt)) == "yes":
  while more_bidders == "yes":
    clear()
    add_to_dictionary(bidders)
    if (more_bidders := remaining_bidders(more_bidders_prompt)) == "no":
      determine_winner(bidders)
