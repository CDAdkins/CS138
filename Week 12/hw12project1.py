from dice import Dice

def main():
    d = Dice()
    print(d.values())
    print(d.score())
    d.roll([4])
    print(d.values())
    print(d.score())
    d.roll([4])
    print(d.values())
    print(d.score())

main()