# Number
number = 4
type_of_number = type(number)
print(f"The type of {number} is {type_of_number}")
# Number is immutable, so we cannot change it in place.
# number += 1 # This would create a new object.

# String
text = "hello"
type_of_text = type(text)
print(f"The type of '{text}' is {type_of_text}")
# String is immutable, so we cannot change it in place.
# text[0] = "H" # This would raise an error.

# Float
floating_point = 4.5
type_of_floating_point = type(floating_point)
print(f"The type of {floating_point} is {type_of_floating_point}")
# Float is immutable, so we cannot change it in place.
# floating_point += 0.5 # This would create a new object.

# Boolean
boolean_value = True
type_of_boolean = type(boolean_value)
print(f"The type of {boolean_value} is {type_of_boolean}")
# Boolean is immutable, so we cannot change it in place.
# boolean_value = not boolean_value # This would create a new object.

# Complex Number
complex_number = 3 + 4j
type_of_complex_number = type(complex_number)
print(f"The type of {complex_number} is {type_of_complex_number}")
# Complex number is immutable, so we cannot change it in place.
# complex_number += 1 + 1j # This would create a new object.

# List
list_value = [1, 2, 3]
type_of_list = type(list_value)
print(f"The type of {list_value} is {type_of_list}")
# List is mutable, so we can change it in place.
list_value.append(4)	
print(f"After appending, the list is now {list_value}")

# Tuple
tuple_value = (1, 2, 3)
type_of_tuple = type(tuple_value)
print(f"The type of {tuple_value} is {type_of_tuple}")
# Tuple is immutable, so we cannot change it in place.
# Tuple cannot be changed in place.
# tuple_value[0] = 0 # This would raise an error.

# Set
# Set is a collection of unique elements.
set_value = {1, 2, 3}
type_of_set = type(set_value)
print(f"The type of {set_value} is {type_of_set}")
# Set is mutable, so we can change it in place.
set_value.add(4)
print(f"After adding, the set is now {set_value}")

# Dictionary
dictionary_value = {"a": 1, "b": 2}
type_of_dictionary = type(dictionary_value)
print(f"The type of {dictionary_value} is {type_of_dictionary}")
# Dictionary is mutable, so we can change it in place.
dictionary_value["c"] = 3
print(f"After adding, the dictionary is now {dictionary_value}")

# Python is dynamically typed, so we don't need to declare types explicitly.
# One type can store different types in istelf.

print("hello world")

# This file demonstrates various data types in Python and prints their types.

# Example of type mismatch
name = "John"
age = 30
# name_age = name + age # This will raise an error because we cannot concatenate str and int directly.
name_age = name + str(age) # Correct way to concatenate
print(f"Name and age concatenated: {name_age}")


#Type conversion functions
'''
This functions converts any data type to given data type
    int()
    float()
    tuple()
    list()
    set()
    dict()
'''