import random
d = range(1, 7)


def roll():
    try:
        input('Roll the dice?(Y/N):')
    except Exception:
        print('Please select only between Y or N')
    print(random.randint(1, 6))


roll()
