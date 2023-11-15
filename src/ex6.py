from TaxMan import TaxMan

def main():
    items = [
            {"id": 1, "desc": "clock", "price": 1.00},
            {"id": 2, "desc": "socks", "price": 2.00},
            {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())

        

if __name__ == '__main__':
    main()