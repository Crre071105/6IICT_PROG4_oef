from multiprocessing.sharedctypes import Value
from xml.dom.minidom import Element


lijst_lijst = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10]
]
# for key in lijst_lijst:
#     for element in key:
#         print(element)
lijst_dict = [
    {'foo':12, 'bar':14 },
    {'moo':52, 'car':641},
    {'doo':6 , 'tar':84, 'var':38 }
]
# for dir in lijst_dict:
#     for key,value in dir.items():
#         print(key,value)

dict_dict = {
    1: {'naam': 'John',  'leeftijd': 27, 'geslacht': 'Man'},
    2: {'naam': 'Marie', 'leeftijd': 22, 'geslacht': 'Vrouw'},
    3: {'naam': 'Kurt',  'leeftijd': 23}
}

for key in dict_dict:
    for key, value in dict_dict[key].items():
        print(key,value)