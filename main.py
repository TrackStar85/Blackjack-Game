from random import randint

from deck import card_name, card_value, end_turn_status, end_game_status

def main():
    ''' User's turn, dealer's turn, and winnder '''
    print('-----------')
    print('YOUR TURN')
    print('-----------')

    user_hand = 0
    drawn_count = 0
    hit = 'y'
    while hit == 'y':
        card_rank = randint(1, 13)
        print('Drew a ' + card_name(card_rank))

        user_hand += card_value(card_rank)
        drawn_count += 1

        if user_hand >= 21:
            hit = 'n'
        elif drawn_count >= 2:
            hit = input('You have ' + str(user_hand) + '. Hit (y/n)? ')

    print('Final hand: ' + str(user_hand) + '.')
    print(end_turn_status(user_hand))


    print('-----------')
    print('DEALER TURN')
    print('-----------')

    dealer_hand = 0 
    drawn_count = 0 

    while dealer_hand <= 17:
        if drawn_count >= 2:
            print('Dealer has ' + str(dealer_hand) + '.')
        card_rank = randint(1, 13)
        print('Drew a ' + card_name(card_rank))
        dealer_hand += card_value(card_rank)
        drawn_count += 1

    print('Final hand: ' + str(dealer_hand) + '.')
    print(end_turn_status(dealer_hand))

    # The final game standings.
    print('-----------')
    print('GAME RESULT')
    print('-----------')

    print(end_game_status(user_hand, dealer_hand))


if __name__ == "__main__":
    main()
