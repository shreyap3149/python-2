class TaxMan:
    def __init__(self, items, tax):
        self.items = items
        self.tax = float(tax.strip('%')) / 100
        self.total = 0
    def calc_total(self):
        subtotal = 0
        for item in self.items:
            
            subtotal += item['price']
            
    
        subtotal *= (1 + self.tax)
        self.total = subtotal
        

    def get_total(self):
        return self.total
        

