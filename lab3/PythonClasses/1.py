class String: 
    def __init__(self): 
        self.input_str = "" 
    def getString(self): 
        self.input_str = input() 
    def printString(self): 
        Upper = self.input_str.upper()  
        print(Upper) 

operation = String() 
operation.getString() 
operation.printString() 
    