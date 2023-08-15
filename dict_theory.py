
# dict
# словник - це структура даних, яка складається з незмінного ключа та будь-якого значення
# значенням може бути інший словник
# словники бажано створювати для зберігання інформації за її змістом чи походженням
person1 = {'name': 'Igor', 'age': 18, 'best_friend': 'Igor'}

person = {
    'name': 'Igor',
    'age': 18,
    'best_friend': 'Igor',
}

empty = None

team = {
    'members_count': 45,
    'sport_types': [
        'chess',
        'soccer',
        'archery',
    ],
    'misty_data': None,
}

set1 = {1, 2, 3, 'hyuf'}

dict_creation_2 = dict()
dict_creation_3 = dict(city='Odesa', village='Myrne')
dict_creation_4 = {}
dict_creation_5 = dict.fromkeys(set1, None)  # другий аргумент буде переданий як значення для всіх
# ключів новоствореного словника, інакше None
print('from keys', dict_creation_5)

# київстар віддаленого_абонента підключи мама     войдюк_і_с_098545454
# git      remote                  add   origin   https://github.com/smartguy-coder/group10072023

# київстар  завантаж на телефон     від мами              смс
#                                войдюк_і_с_098545454
# git       pull                     origin               main
#                            https://github.com/smartguy-coder/group10072023
