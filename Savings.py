class Savings:
    def __init__(self, initial=0):
        self.amount = initial

    def add_savings(self, amount):
        self.amount += amount
        print(f"Savings updated: ${self.amount}")

    def get_savings(self):
        return self.amount
