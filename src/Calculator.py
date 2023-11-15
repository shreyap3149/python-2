class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.result = 0
        

    def add(self):
        self.result = (int(self.first) + int(self.second))
        

    def sub(self):
        self.result = (int(self.first) - int(self.second))
        
    def mul(self):
        self.result = (int(self.first) * int(self.second))
        

    def div(self):
       self.result = (int(self.first) / int(self.second))

    def get_result(self):
        return self.result