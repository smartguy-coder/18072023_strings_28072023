# data = [5, 8, 8]
# set_data = {item for item in data}
# print(set_data)
#
# list_data = [item * 2 for item in data]
# print(list_data)
#
# dict_data = {item: item for item in data}
# print(dict_data)
#
#
# generator_data = (item for item in data)
# print(generator_data)
#
# print(next(generator_data))
# print(next(generator_data))
# data[2] = 200
# print(next(generator_data))


def our_generator():
    print(1111111111111)
    yield 55
    print(222222222222222)
    yield 58
    print(333333333333333)
    yield 100
    print(444444444444)

generated_obj = our_generator()

print(next(generated_obj))
print(999999999999)
print(next(generated_obj))
print(next(generated_obj))
print(next(generated_obj))