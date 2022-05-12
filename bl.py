from random import randint

# Write all of your code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
print("-----------\nYOUR TURN\n-----------")
user_hand = 0
drawn_count = 0
hit = True
while hit:
  card_rank = randint(1, 13)
  if card_rank == 1:
    card_name = 'Ace'
    card_value = 11
  elif card_rank == 11:
    card_name = 'Jack'
    card_value = 10
  elif card_rank == 12:
    card_name = 'Queen'
    card_value = 10
  elif card_rank == 13:
    card_name = 'King'
    card_value = 10
  else:
    card_name = card_rank
    card_value = card_rank
    
  print('Drew a ' + str(card_name))
  user_hand += card_value
  drawn_count = drawn_count + 1
  
  if user_hand >= 21:
    hit = False
  elif drawn_count >= 2:
    hit = input('You have ' + str(user_hand) + '. Hit (y/n)? ') == 'y'

print('Final hand: ' + str(user_hand) + '.')
if user_hand == 21:
  print('BLACKJACK!')
elif user_hand > 21:
  print('BUST.')

print("-----------\nDEALER TURN\n-----------")

dealer_hand = 0 
drawn_count = 0 

while dealer_hand <= 17:
  if drawn_count >= 2:
    print('Dealer has ' + str(dealer_hand) + '.')
  
  card_rank = randint(1, 13)
  if card_rank == 1:
    card_name = 'Ace'
    card_value = 11
  elif card_rank == 11:
    card_name = 'Jack'
    card_value = 10
  elif card_rank == 12:
    card_name = 'Queen'
    card_value = 10
  elif card_rank == 13:
    card_name = 'King'
    card_value = 10
  else:
    card_name = str(card_rank)
    card_value = card_rank

  print('Drew a ' + card_name)
  dealer_hand += card_value
  drawn_count += 1

print('Final hand: ' + str(dealer_hand) + '.')
if dealer_hand == 21:
  print('BLACKJACK!')
elif dealer_hand > 21:
  print('BUST.')

print("-----------\nGAME RESULT\n-----------")

if user_hand == dealer_hand:
  print("Tie.")
elif user_hand == 21 or (user_hand > dealer_hand and user_hand <= 21):
  print("You win!")
elif dealer_hand == 21 or (dealer_hand > user_hand and dealer_hand <= 21):
  print("Dealer wins!")
elif user_hand > 21 and dealer_hand > 21:
  print("Tie.")
elif user_hand == 21 and dealer_hand == 21:
    print("Tie.")
elif user_hand > 21 and dealer_hand <= 21:
    print("Dealer wins!")
elif dealer_hand > 21 and user_hand <= 21:
    print("You win!")
  
  