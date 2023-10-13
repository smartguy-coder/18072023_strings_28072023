# text = '125map   MaP'
#
# cont_map = 'map' in text
# print(cont_map)
#
# cont_map = text.count('map')
# print(cont_map)

import re

text = 'Василь would like to buy thmhpppis map5555555556. Map is 9useful5536. mappi5ng map38 mop68'
# print(text)
# match = re.findall('map', text)
# print(match)

# match = re.findall('[mM]ap', text)
# print(match)

# match = re.findall('^[mM]ap', text)
# print(match)
# match = re.findall('[mM]ap$', text)
# print(match)

# match = re.findall(r'\b[mM]ap\b', text)
# print(match)
# match = re.findall(r'\Bpp\B', text)
# print(match)
# match = re.findall(r'm.p', text)
# print(match)
# match = re.findall(r'm.p\d', text)
# print(match)
# match = re.findall(r'm.p\D', text)
# print(match)
# match = re.findall(r'm.p\D', text)
# print(match)
# match = re.findall(r'5{2,}\d{3}', text)
# print(match)
match = re.findall(r'^[а-яА-ЯA-Z0-9]{5}ь', text)
print(match)