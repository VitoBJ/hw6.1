my_dict = {'Vital': 1987, 'Mil':1986, 'Nif Nif': 1980}
print(my_dict)
print(my_dict['Nif Nif'])
print(my_dict.get('белый заяц'))
my_dict['Nuf Nuf'] =1979
print(my_dict)
my_dict.update({'Naf Naf':1978, 'Seriy Volk': 1970})
print(my_dict)
a=my_dict.pop('Vital')
print(my_dict)
print(a)
my_set={1,2,3,'что то',3,2,1}
print(my_set)
my_set.update({'сложно пока и времени мало',(4,5,6)})
print(my_set)
my_set.discard(2)
print(my_set)
