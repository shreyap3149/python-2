from dataclasses import dataclass
from pprint import pprint

@dataclass
class Invoice:
    invoice_id: str
    user_id: str
    amount: str
    paid: str

  
    
invoices = []
data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]

for x in data:
    invoice_id, user_id, amount, paid = [y.strip() for y in x.split(",")]
    invoices.append(Invoice(invoice_id, user_id, amount, paid))


for q in invoices:
    print(q)