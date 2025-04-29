from Budget import Budget
from FinancePlanner import FinancePlanner
from Savings import Savings

def main():
    print("Welcome to the Pet-Friendly Travel Budget App!")
    budget = Budget(2000)
    planner = FinancePlanner(budget)
    savings = Savings(100)

    planner.plan_trip("Brisbane", 500)
    savings.add_savings(50)

if __name__ == "__main__":
    main()
