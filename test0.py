from Deck import Deck
from Wallet import Wallet
from Hand import Hand

deck = Deck()

player_1 = Hand('Player 1')
the_dealer = Hand('The Dealer')

player_1_account = Wallet('Player', 1000)

print('Welcome to Blackjack!')

def normal_play(hand):

    global hand_on

    while not hand.over21():
        player_decision = input('Do you want to stand or hit?').lower()

        if player_decision == 'hit':
            hand.add_card(deck.deal_one_card())
            print(hand.cards)

            if hand.over21():
                print('Bust! Player 1 went over! The Dealer won!')
                player_1_account.lost_bet()
                hand_on = False

        if player_decision == 'stand':

            dealer_only_normal_play()

            break

def dealer_only_normal_play():

    global hand_on

    print("The Dealer's cards:", the_dealer.cards)

    while the_dealer.sum < 17:
        the_dealer.add_card(deck.deal_one_card())
        print("The Dealer's cards:", the_dealer.cards)

        if the_dealer.over21():
            print('Bust! The Dealer went over! Player 1 won!')
            player_1_account.won_bet()
            hand_on = False
            break

def normal_split_play(hand):

    global hand_on

    while not hand.over21():
        player_decision = input('Do you want to stand or hit?').lower()

        if player_decision == 'hit':
            hand.add_card(deck.deal_one_card())
            print(hand.cards)

            if hand.over21():
                print('Bust! Player 1 went over! The Dealer won!')
                player_1_account.lost_bet()
                hand_on = False

        if player_decision == 'stand':
            break

game_on = True
while game_on:

    player_1.reset()
    the_dealer.reset()
    deck.reset()
    deck.shuffle()

    take_insurance_bet = 'no'
    split_pairs = 'no'

    player_1_account.bet()
    player_1.add_card(deck.deal_one_card())
    the_dealer.add_card(deck.deal_one_card())
    player_1.add_card(deck.deal_one_card())
    the_dealer.add_card(deck.deal_one_card())
    print('Your cards: ', player_1.cards)
    print("The Dealer's second card:", the_dealer.cards[1], ". You cannot see its first card.")

    hand_on = True
    while hand_on:

        if player_1.sum == 21:
            print('Blackjack!')

        if the_dealer.cards[1].rank == 'Ace':

            while True:
                take_insurance_bet = input('Do you want to make an insurance bet?').lower()

                if take_insurance_bet == 'yes':
                    player_1_account.insurance_bet()
                    break

                if take_insurance_bet == 'no':
                    break

        if player_1.sum == 21 and the_dealer.cards[1].rank != 'Ace':
            player_1_account.won_bet_blackjack()
            break

        if player_1.sum == 21 and the_dealer.cards[1].rank == 'Ace':

            pass

        while True:
            double_down = input('Do you want to double down? This is your only chance!').lower()

            if double_down == 'yes':
                player_1.add_card(deck.deal_one_card())
                print('Your cards: ', player_1.cards)

                if player_1.over21():
                    print('Bust! Player 1 went over! The Dealer won!')
                    player_1_account.lost_double_down_bet()

                else:
                    print("The Dealer's cards:", the_dealer.cards)

                    while the_dealer.sum < 17:
                        the_dealer.add_card(deck.deal_one_card())
                        print("The Dealer's cards:", the_dealer.cards)

                        if the_dealer.over21():
                            print('Bust! The Dealer went over! Player 1 won!')
                            player_1_account.won_double_down_bet_or_2_split_bets()
                            hand_on = False
                            break

                    if not the_dealer.over21() and not player_1.over21():

                        if player_1.total_sum() < the_dealer.total_sum():
                            print('The Dealer is closer to 21 than Player 1! The Dealer won!')
                            player_1_account.lost_double_down_bet()

                        elif player_1.total_sum() == the_dealer.total_sum():
                            print('Push! Tie game, no one won!')

                        elif player_1.total_sum() > the_dealer.total_sum():
                            print('Player 1 is closer to 21 than The Dealer! Player 1 won!')
                            player_1_account.won_double_down_bet_or_2_split_bets()
                break

            if double_down == 'no':
                break

        if double_down == 'yes':
            break

        if double_down == 'no' and player_1.cards[0].value == player_1.cards[1].value:

            while True:
                split_pairs = input('Do you want to split pairs? This is your only chance!').lower()

                if split_pairs == 'yes':

                    split_hand_1 = Hand('Player 1 split hand #1')
                    split_hand_1.add_card(player_1.cards[0])
                    split_hand_1.add_card(deck.deal_one_card())
                    print("Your first hand's cards: ", split_hand_1.cards)
                    normal_split_play(split_hand_1)

                    split_hand_2 = Hand('Player 1 split hand #2')
                    split_hand_2.add_card(player_1.cards[1])
                    split_hand_2.add_card(deck.deal_one_card())
                    print("Your second hand's cards: ", split_hand_2.cards)
                    normal_split_play(split_hand_2)

                    print("The Dealer's cards:", the_dealer.cards)

                    if not split_hand_1.over21() and not split_hand_2.over21():

                        while the_dealer.sum < 17:
                            the_dealer.add_card(deck.deal_one_card())
                            print("The Dealer's cards:", the_dealer.cards)

                            if the_dealer.over21():
                                print('Bust! The Dealer went over! Player 1 won!')
                                player_1_account.won_bet()
                                player_1_account.won_bet()
                                hand_on = False
                                break

                    if not split_hand_1.over21() and split_hand_2.over21():

                        while the_dealer.sum < 17:
                            the_dealer.add_card(deck.deal_one_card())
                            print("The Dealer's cards:", the_dealer.cards)

                            if the_dealer.over21():
                                print('Bust! The Dealer went over! Player 1 won!')
                                player_1_account.won_bet()
                                hand_on = False
                                break

                    if split_hand_1.over21() and not split_hand_2.over21():

                        while the_dealer.sum < 17:
                            the_dealer.add_card(deck.deal_one_card())
                            print("The Dealer's cards:", the_dealer.cards)

                            if the_dealer.over21():
                                print('Bust! The Dealer went over! Player 1 won!')
                                player_1_account.won_bet()
                                hand_on = False
                                break

                    if not the_dealer.over21() and not split_hand_1.over21():

                        if split_hand_1.total_sum() < the_dealer.total_sum():
                            print('Hand #1: The Dealer is closer to 21 than Player 1! The Dealer won!')
                            player_1_account.lost_bet()
                            hand_on = False

                        elif split_hand_1.total_sum() == the_dealer.total_sum():
                            print('Hand #1: Push! Tie game, no one won!')
                            hand_on = False

                        elif split_hand_1.total_sum() > the_dealer.total_sum():
                            print('Hand #1: Player 1 is closer to 21 than The Dealer! Player 1 won!')
                            player_1_account.won_bet()
                            hand_on = False

                    if not the_dealer.over21() and not split_hand_2.over21():

                        if split_hand_2.total_sum() < the_dealer.total_sum():
                            print('Hand #2: The Dealer is closer to 21 than Player 1! The Dealer won!')
                            player_1_account.lost_bet()
                            hand_on = False

                        elif split_hand_2.total_sum() == the_dealer.total_sum():
                            print('Hand #2: Push! Tie game, no one won!')
                            hand_on = False

                        elif split_hand_2.total_sum() > the_dealer.total_sum():
                            print('Hand #2: Player 1 is closer to 21 than The Dealer! Player 1 won!')
                            player_1_account.won_bet()
                            hand_on = False

                    break

                if split_pairs == 'no':
                    break

        if split_pairs == 'yes':
            break

        normal_play(player_1)

        if not the_dealer.over21() and not player_1.over21():

            if player_1.total_sum() < the_dealer.total_sum():
                print('The Dealer is closer to 21 than Player 1! The Dealer won!')
                player_1_account.lost_bet()
                hand_on = False

            elif player_1.total_sum() == the_dealer.total_sum():
                print('Push! Tie game, no one won!')
                hand_on = False

            elif player_1.total_sum() > the_dealer.total_sum():
                print('Player 1 is closer to 21 than The Dealer! Player 1 won!')
                player_1_account.won_bet()
                hand_on = False

        if take_insurance_bet == 'yes':

            if the_dealer.cards[0].value == 10:
                print('Player 1 won the insurance bet!')
                player_1_account.won_bet_insurance()

            else:
                print('Player 1 lost the insurance bet!')
                player_1_account.lost_bet_insurance()

    while True:
        play_again = input('Do you want to play again?')

        if play_again.lower() == 'yes':
            game_on = True
            break

        if play_again.lower() == 'no':
            print('See you next time!')
            game_on = False
            break