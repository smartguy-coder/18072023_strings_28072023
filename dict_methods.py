from pprint import pprint

class_info = {
    'name': '5C',
    'quantity_of_pupils': 32,
    'average_score': 11.3,
    'class_teacher': 'Валентина Іванівна',
    'hobbies': [
        'chess',
        'tennis',
        'soccer',
    ],
    'furniture': {
        'type': 'wardrobe',
        'cost': 10000.00,
    },
    'list_of_pupils': [
        'Bobrenko Sasha',
        'Bobrenko2',
        'Bobrenko3',
        'Bobrenko4',
        'Bobrenko5',
        'Bobrenko6',
        ...
    ],
    # 'major_pupil': 'Bobrenko',
}

quantity_pupils = class_info['quantity_of_pupils']
# print(quantity_pupils)
cost = class_info['furniture']['cost']
# print(cost)
hobby = class_info['hobbies'][-1]
# print(hobby)

# major_pupil = class_info.get('major_pupil', class_info['list_of_pupils'][0])
major_pupil = class_info.get('major_pupil', '')
# print(major_pupil)
# print(major_pupil + '!!!!')

# pprint(class_info, width=50)

class_info.setdefault('major_pupil', 'Max')
# pprint(class_info)

# print(class_info['major_pupil'])


class_info['rang'] = 'brilliant'
# pprint(class_info)

class_info['rang'] = 'wooden'

# pprint(class_info)

# for key in class_info:
#     print(key, class_info[key])
#     print('*' * 20)

# print(class_info.keys())
# print(class_info.values())
print(class_info.items())

pair1 = 'name', '5C'
key, value, *other_data = pair1

print(other_data)
print(pair1)
pair2 = ('name', '5C')
key2, value2 = pair2
print(pair2)
tuple_try = (5,)
print(tuple_try)


for key, value in class_info.items():
    print(key, value)
    print('*' * 20)


# delete
del class_info['rang']

our_major_pupil = class_info.pop('major_pupil')
print(f'Thank you, {our_major_pupil}, you was the best leader')

last_pair = class_info.popitem()
print(last_pair)

class_info.clear()

print(class_info)
