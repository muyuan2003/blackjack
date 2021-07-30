from Deck import Deck
from Wallet import Wallet
from Hand import Hand

deck = Deck()

player_1_hand = Hand('Player 1')
the_dealer = Hand('The Dealer')

player_1_account = Wallet('Player', 1000)

print('Welcome to Blackjack!')

def normal_play(hand):

    global hand_on

    while not hand.over21():
        player_decision = input('Do you want to stand or hit?').lower()

        if player_decision == 'hit':
            hand.add_card(deck.deal_one_card())
            print('Your cards:', hand.cards)

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

    while the_dealer.total_sum() < 17:
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

def compare_player_and_dealer(hand):

    global hand_on

    if hand.total_sum() < the_dealer.total_sum():
        print('The Dealer is closer to 21 than Player 1! The Dealer won!')
        player_1_account.lost_bet()
        hand_on = False

    elif hand.total_sum() == the_dealer.total_sum():
        print('Push! Tie game, no one won!')
        hand_on = False

    elif hand.total_sum() > the_dealer.total_sum():
        print('Player 1 is closer to 21 than The Dealer! Player 1 won!')
        player_1_account.won_bet()
        hand_on = False

game_on = True
while game_on:

    player_1_hand.reset()
    the_dealer.reset()
    deck.reset()
    deck.shuffle()

    take_insurance_bet = 'no'
    split_pairs = 'no'

    player_1_account.bet()
    player_1_hand.add_card(deck.deal_one_card())
    the_dealer.add_card(deck.deal_one_card())
    player_1_hand.add_card(deck.deal_one_card())
    the_dealer.add_card(deck.deal_one_card())
    print('Your cards: ', player_1_hand.cards)
    print("The Dealer's second card:", the_dealer.cards[1], ". You cannot see its first card.")

    hand_on = True
    while hand_on:

        if player_1_hand.sum == 21:
            print('Blackjack!')

            if the_dealer.cards[1].rank == 'Ace':

                while True:
                    take_insurance_bet = input('Do you want to make an insurance bet?').lower()

                    if take_insurance_bet == 'yes':
                        player_1_account.insurance_bet()
                        print("The Dealer's cards:", the_dealer.cards)
                        if the_dealer.cards[0].value == 10:
                            print('Player 1 won the insurance bet!')
                            player_1_account.won_bet_insurance()

                        else:
                            print('Player 1 lost the insurance bet!')
                            player_1_account.lost_bet_insurance()

                        break

                    if take_insurance_bet == 'no':
                        break

            print("The Dealer's cards:", the_dealer.cards)

            if the_dealer.total_sum() == 21:
                print('The Dealer also has a blackjack! Push! Tie game, no one won!')
                break
            else:
                player_1_account.won_bet_blackjack()
                break

        if the_dealer.cards[1].rank == 'Ace':

            while True:
                take_insurance_bet = input('Do you want to make an insurance bet?').lower()

                if take_insurance_bet == 'yes':
                    player_1_account.insurance_bet()
                    break

                if take_insurance_bet == 'no':
                    break

        while True:
            double_down = input('Do you want to double down? This is your only chance!').lower()

            if double_down == 'yes':
                player_1_hand.add_card(deck.deal_one_card())
                print('Your cards: ', player_1_hand.cards)

                if player_1_hand.over21():
                    print('Bust! Player 1 went over! The Dealer won!')
                    player_1_account.lost_double_down_bet()

                else:
                    print("The Dealer's cards:", the_dealer.cards)

                    while the_dealer.total_sum() < 17:
                        the_dealer.add_card(deck.deal_one_card())
                        print("The Dealer's cards:", the_dealer.cards)

                        if the_dealer.over21():
                            print('Bust! The Dealer went over! Player 1 won!')
                            player_1_account.won_double_down_bet_or_2_split_bets()
                            hand_on = False
                            break

                    if not the_dealer.over21() and not player_1_hand.over21():

                        compare_player_and_dealer(player_1_hand)
                break

            if double_down == 'no':
                break

        if double_down == 'yes':
            break

        if double_down == 'no' and player_1_hand.cards[0].value == player_1_hand.cards[1].value:

            while True:
                split_pairs = input('Do you want to split pairs? This is your only chance!').lower()

                if split_pairs == 'yes':

                    player_1_split_hand_1 = Hand('Player 1 split hand #1')
                    player_1_split_hand_1.add_card(player_1_hand.cards[0])
                    player_1_split_hand_1.add_card(deck.deal_one_card())
                    print("Your first hand's cards: ", player_1_split_hand_1.cards)
                    normal_split_play(player_1_split_hand_1)

                    player_1_split_hand_2 = Hand('Player 1 split hand #2')
                    player_1_split_hand_2.add_card(player_1_hand.cards[1])
                    player_1_split_hand_2.add_card(deck.deal_one_card())
                    print("Your second hand's cards: ", player_1_split_hand_2.cards)
                    normal_split_play(player_1_split_hand_2)

                    print("The Dealer's cards:", the_dealer.cards)

                    if not player_1_split_hand_1.over21() and not player_1_split_hand_2.over21():

                        while the_dealer.total_sum() < 17:
                            the_dealer.add_card(deck.deal_one_card())
                            print("The Dealer's cards:", the_dealer.cards)

                            if the_dealer.over21():
                                print('Bust! The Dealer went over! Player 1 won!')
                                player_1_account.won_double_down_bet_or_2_split_bets()
                                hand_on = False
                                break

                    if not player_1_split_hand_1.over21() and player_1_split_hand_2.over21():
                        dealer_only_normal_play()

                    if player_1_split_hand_1.over21() and not player_1_split_hand_2.over21():
                        dealer_only_normal_play()

                    if not the_dealer.over21() and not player_1_split_hand_1.over21():
                        print('Hand #1:')

                        compare_player_and_dealer(player_1_split_hand_1)

                    if not the_dealer.over21() and not player_1_split_hand_2.over21():
                        print('Hand #2:')

                        compare_player_and_dealer(player_1_split_hand_2)

                    break

                if split_pairs == 'no':
                    break

        if split_pairs == 'yes':
            break

        normal_play(player_1_hand)

        compare_player_and_dealer(player_1_hand)

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