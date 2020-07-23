my_dict = {
    'satheesh': 'name', '9989884111': 'phoneno'
}

# Use to invert dictionaries that have unique values
# my_inverted_dict = dict(map(reversed, my_dict.items()))

print(my_dict.items())
# print(my_inverted_dict)


my_inverted_dict = dict()
for key, value in my_dict.items():
    (my_inverted_dict.setdefault(value, list()).append(key))

print(my_inverted_dict)
