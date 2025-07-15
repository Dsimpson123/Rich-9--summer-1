# The amount of money we have to spend
funds = 2500

# A dictonary of ou items we are spending our budget on;
budgets = {}
expenses = {}

def AddBudget(name, amount):
    global funds
    if name in budgets:
        raise ValueError("Budget for item already exists")
    if amount > funds:
        raise ValueError("No can do, you are to broke")
    budgets[name] = amount
    funds -= amount
    expenses[name] = 0
    return funds

def Spend(name, amount):
    if name not in expenses:
        raise ValueError("Item not in budget")
    expenses[name] += amount
    budgeted = budgets[name]
    spent = expenses[name]
    return budgeted - spent

def PrintBudget():
    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        remainingBudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} '
              f'{remainingBudget:10.2f}')


print("Total funds" , funds)
AddBudget("Books", 100)
AddBudget("Rent", 800)
AddBudget("Car Note", 200)

Spend("Books", 50)
Spend("Rent", 800)
Spend("Car Note", 200)

PrintBudget()