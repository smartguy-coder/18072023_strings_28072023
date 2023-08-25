from random import randint, seed, random, choice

import library


def main():
    meters = 6
    result = library.convert_meters_to_inches(meters)
    print(f'{meters} meters = {result} inches')


if __name__ == '__main__':
    # seed(1111)
    main()
    print(randint(1, 4))
    print(random())
    professions = ['teacher', 'doctor']
    print(choice(professions))
    print()
