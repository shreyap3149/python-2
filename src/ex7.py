from Calculator import Calculator

def main():

    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())

if __name__ == '__main__':
    main()