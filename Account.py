class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.bet_amount = 0

    def __str__(self):
        return 'Account owner: {}\nAccount balance: {}$'.format(self.owner, self.balance)

    def bet(self):
        while True:
            self.bet_amount = int(input('How much do you want to bet for this game? Please enter a number.'))
            if self.balance >= self.bet_amount:
                print('Good bet!')
                break
            else:
                print('You do not have the necessary funds to make this bet. Please pick a lower amount.')

    def won_bet(self):
        self.balance += self.bet_amount
        print('You now have {}$ after winning this bet'.format(self.balance))

    def lost_bet(self):
        self.balance -= self.bet_amount
        print('You now have {}$ after losing this bet'.format(self.balance))


