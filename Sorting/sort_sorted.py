# SORTING TUPLE AND SET
number_tuple = (1,4,0,2,5,6)
number_set = {5,5,10,1,0}

number_tuple_sorted = sorted(number_tuple)
number_set_sorted = sorted(number_set)

print(number_tuple_sorted)
print(number_set_sorted)

print(tuple(number_tuple_sorted))
print(set(number_set_sorted))

#SORTING STRING
string_number_value = '34521'
string_value = 'I like to sort'
sorted_string_number = sorted(string_number_value)
sorted_string = sorted(string_value)
print(sorted_string_number)
print(sorted_string)

#sorted() With a key Argument
words = ['banana', 'pie', 'Washington', 'book']
print(sorted(words, key=len))

names_with_case = ['harry', 'Suzy', 'al', 'Mark']
print(sorted(names_with_case))
print(sorted(names_with_case, key=str.lower))

#sort examples
phrases = ['when in rome', 
        'what goes around comes around', 
        'all is fair in love and war'
        ]

phrases.sort(key=lambda x: x.split()[2][1], reverse=True)
print(phrases)
