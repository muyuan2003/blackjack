import random
print('Welcome to Blackjack!')

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

    def __repr__(self):
        return str(self)


class Deck():

    def __init__(self):

        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        return self.all_cards.pop()


def take_bet():
    return int(input('How much do you want to bet for this game? Please enter a number.'))


class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.bet_amount = take_bet()

    def __str__(self):
        return 'Account owner: {}\nAccount balance: {}$'.format(self.owner, self.balance)

    def bet(self):
        if self.balance >= self.bet_amount:
            print('Good bet!')
        else:
            print('You do not have the necessary funds to make this bet. Please pick a lower amount.')

    def won_bet(self):
        self.balance += self.bet_amount
        print('You now have {}$ after winning this bet'.format(self.balance))

    def lost_bet(self):
        self.balance -= self.bet_amount
        print('You now have {}$ after losing this bet'.format(self.balance))


class Player():
    def __init__(self, name):
        self.name = name
        self.sum = 0
        self.cards = []

    def add_card(self, new_card):
        self.cards.append(new_card)

    def over21(self):
        self.sum = 0
        for card in self.cards:
            self.sum += card.value
        if 'Ace' not in self.cards:
            if self.sum > 21:
                return True
            else:
                return False
        else:
            number_of_aces = self.cards.count('Ace')
            if self.sum > (21 + 10 * number_of_aces):
                return True
            else:
                return False

    def total_sum(self):
        number_of_aces = self.cards.count('Ace')
        if 'Ace' in self.cards:
            if self.sum > 21:
                for n in range(number_of_aces):
                    self.sum - 10
                    if self.sum < 21:
                        break

        return self.sum


deck = Deck()
player_1_account = Account('Player', 100)
game_on = True


while game_on:
    player_1 = Player('Player 1')
    computer = Player('Computer')
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

    play_again = input('Do you want to play again?')

    if play_again.lower() == 'yes':
        game_on = True
    else:
        print('See you next time!')
        break



