class Player:
    def __init__(self, name):
        self.name = name
        self.sum = 0
        self.cards = []

    def add_card(self, new_card):
        self.cards.append(new_card)
        self.sum += new_card.value

    def over21(self):

        number_of_aces = 0
        for card in self.cards:
            if card.rank == 'Ace':
                number_of_aces += 1

        if number_of_aces == 0:
            if self.sum > 21:
                return True
            else:
                return False
        else:
            if self.sum > (21 + 10 * number_of_aces):
                return True
            else:
                return False

    def total_sum(self):
        number_of_aces = 0

        for card in self.cards:
            if card.rank == 'Ace':
                number_of_aces += 1
        if number_of_aces != 0:
            if self.sum > 21:
                for n in range(number_of_aces):
                    self.sum - 10
                    if self.sum < 21:
                        break

        return self.sum

    def reset(self):
        self.sum = 0
        self.cards = []
