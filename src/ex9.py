from Character import Character
from Fighter import Fighter
from Dwarf import Dwarf

def main():
    f = Fighter(18)
    d = Dwarf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)

if __name__ == '__main__':
    main()
    