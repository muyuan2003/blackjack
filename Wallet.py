class Wallet:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.bet_amount = 0
        self.insurance_bet_amount = 0

    def __str__(self):
        return 'Wallet owner: {}\nWallet balance: {}$'.format(self.owner, self.balance)

    def bet(self):
        while True:
            self.bet_amount = int(input('How much do you want to bet for this game? Please enter a number.'))

            if self.bet_amount <= self.balance:
                print('Good bet!')
                break

            else:
                print('You do not have the necessary funds to make this bet. Please pick a lower amount.')

    def insurance_bet(self):
        while True:
            self.insurance_bet_amount = int(input('How much do you want to bet for this game? Please enter a number.'))

            if self.insurance_bet_amount <= self.balance and self.insurance_bet_amount <= 0.5 * self.bet_amount:
                print('Good bet!')
                break

            elif self.balance >= self.insurance_bet_amount:
                print('Your insurance bet cannot be more than half your main bet. Please pick a lower amount.')

            else:
                print('You do not have the necessary funds to make this bet. Please pick a lower amount.')

    def won_bet(self):
        self.balance += self.bet_amount
        print('You now have {}$ after winning this bet'.format(self.balance))

    def won_double_down_bet_or_2_split_bets(self):
        self.balance += 2 * self.bet_amount
        print('You now have {}$ after winning this bet'.format(self.balance))

    def won_bet_blackjack(self):
        self.balance += 1.5 * self.bet_amount
        print('You now have {}$ after winning this bet'.format(self.balance))

    def won_bet_insurance(self):
        self.balance += 2 * self.insurance_bet_amount
        print('You now have {}$ after winning this bet'.format(self.balance))

    def lost_bet(self):
        self.balance -= self.bet_amount
        print('You now have {}$ after losing this bet'.format(self.balance))

    def lost_double_down_bet(self):
        self.balance -= 2 * self.bet_amount
        print('You now have {}$ after losing this bet'.format(self.balance))

    def lost_bet_insurance(self):
        self.balance -= self.insurance_bet_amount
        print('You now have {}$ after losing this bet'.format(self.balance))

