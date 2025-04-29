class Budget:
    def __init__(self, amount):
        self.total = amount

    def spend(self, amount):
        if amount <= self.total:
            self.total -= amount
            return True
        return False

    def get_balance(self):
        return self.total
