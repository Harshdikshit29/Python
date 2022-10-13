class Calculator:
    
    # constructor
    def  __init__(self, x, y):
        self.x = x
        self.y = y
        
    # instance method
    def add(self):
        return self.x + self.y
    
    def substract(self):
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        return self.x / self.y