from Deck import Deck
from Wallet import Wallet
from Hand import Hand

# Create objects using our classes
deck = Deck()
player_1_hand = Hand('Player 1')
dealer = Hand('The Dealer')
player_1_account = Wallet('Player', 1000)
print('Welcome to Blackjack!')
print('You have 1000$.')


# player_play() lets Player 1 hit until he wants to stand or busts
def player_play():
    global hand_on
    while not player_1_hand.over21():
        player_decision = input('Do you want to stand or hit?').lower()
        if player_decision == 'hit':
            player_1_hand.add_card(deck.deal_one_card())
            print('Your cards:', player_1_hand.cards)
            if player_1_hand.sum == 21:
                print('Blackjack!')
                player_1_account.won_bet_blackjack()
                hand_on = False
                break
            if player_1_hand.over21():
                print('Bust! Player 1 went over! The Dealer won!')
                player_1_account.lost_bet()
                hand_on = False
        if player_decision == 'stand':
            print("The Dealer's cards:", dealer.cards)
            dealer_play()
            break


# dealer_play() lets dealer hit until he has a a count of 17 or more
def dealer_play():
    global hand_on
    while dealer.total_sum() < 17:
        dealer.add_card(deck.deal_one_card())
        print("The Dealer's cards:", dealer.cards)
        if dealer.over21():
            print('Bust! The Dealer went over! Player 1 won!')
            player_1_account.won_bet()
            hand_on = False
            break


# player_split_play() lets Player 1 hit until he wants to stand or busts on a split hand
def player_split_play(hand):
    global hand_on
    while not hand.over21():
        player_decision = input('Do you want to stand or hit?').lower()
        if player_decision == 'hit':
            hand.add_card(deck.deal_one_card())
            print(hand.cards)
            if hand.sum == 21:
                print('Blackjack!')
                hand_on = False
                break
            if hand.over21():
                print('Bust! Player 1 went over! The Dealer won!')
                player_1_account.lost_bet()
                hand_on = False
        if player_decision == 'stand':
            break


# compare_player_and_dealer(hand) compares the sum of hand to the sum of the dealer's hand
def compare_player_and_dealer(hand):
    global hand_on
    if hand.total_sum() < dealer.total_sum():
        print('The Dealer is closer to 21 than Player 1! The Dealer won!')
        player_1_account.lost_bet()
        hand_on = False
    elif hand.total_sum() == dealer.total_sum():
        print('Push! Tie game, no one won!')
        hand_on = False
    else:
        print('Player 1 is closer to 21 than The Dealer! Player 1 won!')
        player_1_account.won_bet()
        hand_on = False


# check_insurance() determines whether or not Player 1 won the insurance bet
def check_insurance():
    if dealer.cards[0].value == 10:
        print('Player 1 won the insurance bet!')
        player_1_account.won_bet_insurance()
    else:
        print('Player 1 lost the insurance bet!')
        player_1_account.lost_bet_insurance()


# Game starts
game_on = True
while game_on:
    player_1_hand.reset()
    dealer.reset()
    deck.reset()
    deck.shuffle()
    take_insurance_bet = 'no'
    split_pairs = 'no'

    # Place bet and deal cards
    player_1_account.bet()
    player_1_hand.add_card(deck.deal_one_card())
    dealer.add_card(deck.deal_one_card())
    player_1_hand.add_card(deck.deal_one_card())
    dealer.add_card(deck.deal_one_card())
    print('Your cards: ', player_1_hand.cards)
    print("The Dealer's second card:", dealer.cards[1], ". You cannot see its first card.")
    hand_on = True
    while hand_on:
        # Player 1 has a blackjack
        if player_1_hand.sum == 21:
            print('Blackjack!')
            if dealer.cards[1].rank == 'Ace':
                while True:
                    take_insurance_bet = input('Do you want to make an insurance bet?').lower()
                    if take_insurance_bet == 'yes':
                        player_1_account.insurance_bet()
                        print("The Dealer's cards:", dealer.cards)
                        if dealer.cards[0].value == 10:
                            print('Player 1 won the insurance bet!')
                            player_1_account.won_bet_insurance()
                        else:
                            print('Player 1 lost the insurance bet!')
                            player_1_account.lost_bet_insurance()
                        break
                    if take_insurance_bet == 'no':
                        break
            print("The Dealer's cards:", dealer.cards)
            if dealer.total_sum() == 21:
                print('The Dealer also has a blackjack! Push! Tie game, no one won!')
                break
            else:
                player_1_account.won_bet_blackjack()
                break

        # Player 1 can choose whether or not to place an insurance bet
        if dealer.cards[1].rank == 'Ace':
            while True:
                take_insurance_bet = input('Do you want to make an insurance bet?').lower()
                if take_insurance_bet == 'yes':
                    player_1_account.insurance_bet()
                    break
                if take_insurance_bet == 'no':
                    break

        # Player 1 chooses whether or not to double down
        while True:
            double_down = input('Do you want to double down? This is your only chance!').lower()
            if double_down == 'yes':
                player_1_hand.add_card(deck.deal_one_card())
                print('Your cards: ', player_1_hand.cards)
                if player_1_hand.sum == 21:
                    print('Blackjack!')
                    player_1_account.won_bet_double_down_blackjack()
                elif player_1_hand.over21():
                    print('Bust! Player 1 went over! The Dealer won!')
                    player_1_account.lost_double_down_bet()
                else:
                    print("The Dealer's cards:", dealer.cards)
                    while dealer.total_sum() < 17:
                        dealer.add_card(deck.deal_one_card())
                        print("The Dealer's cards:", dealer.cards)
                        if dealer.over21():
                            print('Bust! The Dealer went over! Player 1 won!')
                            player_1_account.won_double_down_bet()
                            break
                    if not dealer.over21() and not player_1_hand.over21():
                        compare_player_and_dealer(player_1_hand)
                        compare_player_and_dealer(player_1_hand)
                break
            if double_down == 'no':
                break

        if double_down == 'yes':
            if take_insurance_bet == 'yes':
                check_insurance()
            break

        # Player 1 can choose whether or not to split his hand
        if double_down == 'no' and player_1_hand.cards[0].value == player_1_hand.cards[1].value:
            while True:
                split_pairs = input('Do you want to split pairs? This is your only chance!').lower()
                if split_pairs == 'yes':
                    player_1_split_hand_1 = Hand('Player 1 split hand #1')
                    player_1_split_hand_1.add_card(player_1_hand.cards[0])
                    player_1_split_hand_1.add_card(deck.deal_one_card())
                    print("Your first hand's cards: ", player_1_split_hand_1.cards)
                    if player_1_split_hand_1.sum == 21:
                        print('Blackjack!')
                    else:
                        player_split_play(player_1_split_hand_1)

                    player_1_split_hand_2 = Hand('Player 1 split hand #2')
                    player_1_split_hand_2.add_card(player_1_hand.cards[1])
                    player_1_split_hand_2.add_card(deck.deal_one_card())
                    print("Your second hand's cards: ", player_1_split_hand_2.cards)
                    if player_1_split_hand_2.sum == 21:
                        print('Blackjack!')
                    else:
                        player_split_play(player_1_split_hand_2)

                    print("The Dealer's cards:", dealer.cards)
                    if not player_1_split_hand_1.over21() and not player_1_split_hand_2.over21():
                        while dealer.total_sum() < 17:
                            dealer.add_card(deck.deal_one_card())
                            print("The Dealer's cards:", dealer.cards)
                            if dealer.over21():
                                print('Bust! The Dealer went over! Player 1 won!')
                                player_1_account.won_bet()
                                player_1_account.won_bet()
                                hand_on = False
                                break
                    if not player_1_split_hand_1.over21() and player_1_split_hand_2.over21():
                        dealer_play()
                    if player_1_split_hand_1.over21() and not player_1_split_hand_2.over21():
                        dealer_play()
                    if not dealer.over21() and not player_1_split_hand_1.over21():
                        print('Hand #1:')
                        compare_player_and_dealer(player_1_split_hand_1)
                    if not dealer.over21() and not player_1_split_hand_2.over21():
                        print('Hand #2:')
                        compare_player_and_dealer(player_1_split_hand_2)
                    break
                if split_pairs == 'no':
                    break

        if split_pairs == 'yes':
            if take_insurance_bet == 'yes':
                check_insurance()
            break

        # It is Player 1's turn to choose to stand or hit
        player_play()
        if hand_on:
            compare_player_and_dealer(player_1_hand)

        if take_insurance_bet == 'yes':
            check_insurance()

    # Player 1 can decide whether or not to play again
    while True:
        play_again = input('Do you want to play again?')
        if play_again.lower() == 'yes':
            game_on = True
            break
        if play_again.lower() == 'no':
            print('See you next time!')
            game_on = False
            break
