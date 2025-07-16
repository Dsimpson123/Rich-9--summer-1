#Your task is to convert this program into a class

class budgetManager():
    def __init__(self, amount):
        
        

    # The amount of money we have to spend
        self.funds = amount

    # A dictonary of ou items we are spending our budget on;
        self.budgets = {}

         
        self.expenses = {}

    def AddBudget(self, name, amount):
        global funds
        if name in self.budgets:
            raise ValueError("Budget for item already exists")
        if amount > funds:
            raise ValueError("No can do, you are to broke")
        self.budgets[name] = amount
        funds -= amount
        self.expenses[name] = 0
        return funds

    def Spend(Self, name, amount):
        if name not in self.expenses:
            raise ValueError("Item not in budget")
        Self.expenses[name] += amount
        budgeted = self.budgets[name]
        spent = self.expenses[name]
        return budgeted - spent

    def PrintBudget():
        print("Budget     Budgeted   Spent  Remaining")
        print("---------------------------------------")
        totalBudgeted = 0
        totalSpent = 0
        totalRemaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = self.expenses[name]
            remainingBudget = budgeted - spent
            print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} '
                f'{remainingBudget:10.2f}')
            totalBudgeted += budgeted
            totalSpent += spent
            totalRemaining = remainingBudget
        print(f'{"Total":15s}, {totalBudgeted:10.2f}, {totalSpent:10.2f} '
                f'{totalBudgeted - totalSpent:10.2f}') 

    print("Total funds" , funds)
    AddBudget("Books", 100)
    AddBudget("Rent", 800)
    AddBudget("Car Note", 200)

    Spend("Books", 50)
    Spend("Rent", 800)
    Spend("Car Note", 200)

    PrintBudget()