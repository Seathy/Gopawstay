class FinancePlanner:
    def __init__(self, budget):
        self.budget = budget

    def plan_trip(self, destination, cost):
        if self.budget.spend(cost):
            print(f"Trip to {destination} booked! Remaining balance: ${self.budget.get_balance()}")
        else:
            print("Not enough budget for this trip.")
