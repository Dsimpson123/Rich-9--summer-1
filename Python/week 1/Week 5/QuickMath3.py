class Calculator:
    def Add(self, x, y):
        return x + y
    
    def Sub(self, x, y):
        return x - y
    
    def Multiply(self, x, y):
        return x * y
    
    def Divide(self, x, y):
        return x / y
    
calculator = Calculator()

sum = calculator.Add(25,70)
difference = calculator.Subtract(10,5)
Product = calculator.Multiply(5,5 )
dividend = calculator.Divide(12, 4)

print(sum)
print(difference)
print(dividend)
print(Product)



    