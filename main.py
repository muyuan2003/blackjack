from Deck import Deck
from Account import Account
from Player import Player

deck = Deck()
player_1_account = Account('Player', 100)

player_1 = Player('Player 1')
computer = Player('Computer')
print('Welcome to Blackjack!')
game_on = True

while game_on:
    player_1.reset()
    computer.reset()
    deck.shuffle()
    player_1_account.bet()
    player_1.add_card(deck.deal_one_card())
    player_1.add_card(deck.deal_one_card())
    print('Your cards: ', player_1.cards)

    computer.add_card(deck.deal_one_card())
    computer.add_card(deck.deal_one_card())
    print("The computer's second card:", computer.cards[1], ". You cannot see its first card.")

    while not player_1.over21():
        player_decision = input('Do you want to stand or hit?').lower()
        if player_decision == 'hit':
            player_1.add_card(deck.deal_one_card())
            print(player_1.cards)

        if player_decision == 'stand':

            if computer.total_sum() > player_1.total_sum():
                print("The computer's cards:", computer.cards)
                print('Computer is closer to 21 than Player 1! Computer won!')
                player_1_account.lost_bet()
                break

            while not computer.over21():
                computer.add_card(deck.deal_one_card())
                print("The computer's cards:", computer.cards)
                if computer.over21():
                    print('Computer went over! Player 1 won!')
                    player_1_account.won_bet()
                    break

                if computer.total_sum() > player_1.total_sum():
                    print('Computer is closer to 21 than Player 1! Computer won!')
                    player_1_account.lost_bet()
                    break

            break
    if player_1.over21():
        print('Player 1 went over! Computer won!')
        player_1_account.lost_bet()

    ask_for_another_game = True
    while ask_for_another_game:
        play_again = input('Do you want to play again?')
        if play_again.lower() == 'yes':
            game_on = True
            break
        if play_again.lower() == 'no':
            print('See you next time!')
            game_on = False
            break
