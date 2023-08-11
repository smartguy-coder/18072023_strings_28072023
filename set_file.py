# type1 = 'hghjgjhgj'
# type2 = True
# type2_ = False
# type3 = 5656
# print(id(type3))
# type4 = 5.65
#
# type3 = 1111111111
# print(id(type3))
#
# type5 = [5656, 5656, 'kghkjhkj']
# print(id(type5))
# type5.append(66)
# print(id(type5))

list_similar_elements = [5, 5, 5, 66, 'jhgjhgj']
# set
# В СЕТ МОЖУТЬ ПОПАСТИ ТІЛЬКИ НЕЗМІННІ ОБЄКТИ!!!
# set1 = set()
# print(set1)
#
# set2 = set(list_similar_elements)
# print(set2)
# print(len(set2))
#
# set3 = {6, 5, 5, 'kjhgjh', 88}
# print(set3)
#
# unique_letters = set('gjhgjjgjgjhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
#
# unique_letters.add('Rrrrrrrrr')
# print(unique_letters)
# unique_letters.update('QWERTY')
# unique_letters.update(list_similar_elements)
# print(unique_letters)
# # print(list(unique_letters))
# unique_letters.discard(44444444)
# unique_letters.discard('Q')
# print(unique_letters)
#
# unique_letters.remove('R')
#
# print(unique_letters.pop())

set1 = {1, 2, 3}
set2 = {3, 4, 5}
# # спільні елементи для двох множин
# print('пересічення множин', set1 & set2)
# print('пересічення множин', set1.intersection(set2))
#
# # всі елементи всіх множин
# print('об\'єднання', set1 | set2)
# print('об\'єднання', set1.union(set2))

# залишаються тільки ті елементи першої множини, яких немає в другій множині
print('різниця', set1 - set2)
#
# елементи, які є відмінними для різних множин
print('відмінність', set1 ^ set2)
print('\u0440\u043d\u0430\u0444\u0442')