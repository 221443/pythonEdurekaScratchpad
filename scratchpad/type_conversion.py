"""
Python Type Conversion Comprehensive Guide
==========================================
This script demonstrates converting between all major Python data types
using int(), float(), tuple(), list(), set(), and dict()
"""

# ============================================
# STEP 1: Create variables of different types
# ============================================

print("=" * 60)
print("ORIGINAL VARIABLES")
print("=" * 60)

# Basic types
my_int = 42
my_float = 3.14
my_string = "123"
my_string_text = "hello"
my_bool = True

# Collection types
my_list = [1, 2, 3, 2, 1]
my_tuple = (4, 5, 6, 5, 4)
my_set = {7, 8, 9}
my_dict = {'a': 10, 'b': 20, 'c': 30}

# Special cases
empty_list = []
single_element_list = [100]
nested_list = [[1, 2], [3, 4]]
dict_items = [('x', 1), ('y', 2)]  # List of tuples for dict conversion

print(f"my_int: {my_int} (type: {type(my_int).__name__})")
print(f"my_float: {my_float} (type: {type(my_float).__name__})")
print(f"my_string: {my_string} (type: {type(my_string).__name__})")
print(f"my_string_text: {my_string_text} (type: {type(my_string_text).__name__})")
print(f"my_bool: {my_bool} (type: {type(my_bool).__name__})")
print(f"my_list: {my_list} (type: {type(my_list).__name__})")
print(f"my_tuple: {my_tuple} (type: {type(my_tuple).__name__})")
print(f"my_set: {my_set} (type: {type(my_set).__name__})")
print(f"my_dict: {my_dict} (type: {type(my_dict).__name__})")

# ============================================
# STEP 2: Convert to INT
# ============================================

print("\n" + "=" * 60)
print("CONVERTING TO INT")
print("=" * 60)

# From float to int - truncates decimal part (floor division towards zero)
int_from_float = int(my_float)
print(f"int({my_float}) = {int_from_float}")
print("  → Truncates decimal part, doesn't round")

# From string to int - only works with numeric strings
int_from_string = int(my_string)
print(f"int('{my_string}') = {int_from_string}")
print("  → Parses numeric string to integer")

# From bool to int - True=1, False=0
int_from_bool = int(my_bool)
print(f"int({my_bool}) = {int_from_bool}")
print("  → True becomes 1, False becomes 0")

# What doesn't work with int()
print("\n❌ Cannot convert directly to int:")
try:
    int(my_string_text)
except ValueError as e:
    print(f"  int('{my_string_text}') → ValueError: {e}")

try:
    int(my_list)
except TypeError as e:
    print(f"  int({my_list}) → TypeError: Cannot convert list directly")

try:
    int(my_dict)
except TypeError as e:
    print(f"  int({my_dict}) → TypeError: Cannot convert dict directly")

# ============================================
# STEP 3: Convert to FLOAT
# ============================================

print("\n" + "=" * 60)
print("CONVERTING TO FLOAT")
print("=" * 60)

# From int to float - adds .0
float_from_int = float(my_int)
print(f"float({my_int}) = {float_from_int}")
print("  → Adds decimal point, becoming floating-point number")

# From string to float
float_from_string = float(my_string)
print(f"float('{my_string}') = {float_from_string}")
print("  → Parses numeric string to float")

# From bool to float
float_from_bool = float(my_bool)
print(f"float({my_bool}) = {float_from_bool}")
print("  → True becomes 1.0, False becomes 0.0")

# Special float values
print(f"float('inf') = {float('inf')}  → Positive infinity")
print(f"float('-inf') = {float('-inf')}  → Negative infinity")

# What doesn't work
print("\n❌ Cannot convert directly to float:")
try:
    float(my_list)
except TypeError:
    print(f"  float({my_list}) → TypeError: Cannot convert collections")

# ============================================
# STEP 4: Convert to TUPLE
# ============================================

print("\n" + "=" * 60)
print("CONVERTING TO TUPLE")
print("=" * 60)

# From list to tuple - creates immutable version
tuple_from_list = tuple(my_list)
print(f"tuple({my_list}) = {tuple_from_list}")
print("  → Creates immutable copy of list elements")

# From set to tuple - order may vary
tuple_from_set = tuple(my_set)
print(f"tuple({my_set}) = {tuple_from_set}")
print("  → Converts set to tuple (order not guaranteed)")

# From dict to tuple - only keys are converted
tuple_from_dict = tuple(my_dict)
print(f"tuple({my_dict}) = {tuple_from_dict}")
print("  → Only dictionary KEYS are converted, not values!")

# From string to tuple - each character becomes element
tuple_from_string = tuple(my_string_text)
print(f"tuple('{my_string_text}') = {tuple_from_string}")
print("  → Each character becomes a separate element")

# Single element conversions (non-iterables need special handling)
# Note: You cannot directly convert int/float to tuple
print("\n⚠️  Special cases:")
print(f"  tuple([{my_int}]) = {tuple([my_int])}  → Wrap in list first")
print(f"  ({my_int},) = {(my_int,)}  → Or use comma syntax for single element")

# ============================================
# STEP 5: Convert to LIST
# ============================================

print("\n" + "=" * 60)
print("CONVERTING TO LIST")
print("=" * 60)

# From tuple to list - creates mutable version
list_from_tuple = list(my_tuple)
print(f"list({my_tuple}) = {list_from_tuple}")
print("  → Creates mutable copy of tuple elements")

# From set to list - order may vary
list_from_set = list(my_set)
print(f"list({my_set}) = {list_from_set}")
print("  → Converts set to list (order not guaranteed)")

# From dict to list - only keys
list_from_dict = list(my_dict)
print(f"list({my_dict}) = {list_from_dict}")
print("  → Only dictionary KEYS are converted")

# To get both keys and values:
list_from_dict_items = list(my_dict.items())
print(f"list({my_dict}.items()) = {list_from_dict_items}")
print("  → Use .items() to get key-value pairs as tuples")

# From string to list
list_from_string = list(my_string_text)
print(f"list('{my_string_text}') = {list_from_string}")
print("  → Each character becomes a separate element")

# ============================================
# STEP 6: Convert to SET
# ============================================

print("\n" + "=" * 60)
print("CONVERTING TO SET")
print("=" * 60)

# From list to set - removes duplicates!
set_from_list = set(my_list)
print(f"set({my_list}) = {set_from_list}")
print("  → REMOVES DUPLICATES and loses order!")

# From tuple to set - also removes duplicates
set_from_tuple = set(my_tuple)
print(f"set({my_tuple}) = {set_from_tuple}")
print("  → Removes duplicates from tuple")

# From dict to set - only keys
set_from_dict = set(my_dict)
print(f"set({my_dict}) = {set_from_dict}")
print("  → Only dictionary KEYS are converted")

# From string to set - unique characters
set_from_string = set(my_string_text)
print(f"set('{my_string_text}') = {set_from_string}")
print("  → Creates set of unique characters")

# Demonstrating duplicate removal
duplicate_list = [1, 1, 2, 2, 3, 3]
print(f"\nset({duplicate_list}) = {set(duplicate_list)}")
print("  → Perfect for removing duplicates from any sequence!")

# ============================================
# STEP 7: Convert to DICT
# ============================================

print("\n" + "=" * 60)
print("CONVERTING TO DICT")
print("=" * 60)

# From list of tuples/pairs
dict_from_pairs = dict(dict_items)
print(f"dict({dict_items}) = {dict_from_pairs}")
print("  → List of (key, value) tuples becomes dictionary")

# From zip of two sequences
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
dict_from_zip = dict(zip(keys, values))
print(f"dict(zip({keys}, {values})) = {dict_from_zip}")
print("  → Combines two sequences into key-value pairs")

# From list of lists (each with 2 elements)
list_pairs = [['a', 1], ['b', 2], ['c', 3]]
dict_from_list_pairs = dict(list_pairs)
print(f"dict({list_pairs}) = {dict_from_list_pairs}")
print("  → Nested lists with 2 elements become key-value pairs")

# What doesn't work
print("\n❌ Cannot convert directly to dict:")
try:
    dict(my_list)
except (TypeError, ValueError) as e:
    print(f"  dict({my_list}) → Error: List elements aren't pairs")

try:
    dict(my_set)
except (TypeError, ValueError) as e:
    print(f"  dict({my_set}) → Error: Set elements aren't pairs")

# ============================================
# STEP 8: ADVANCED CONVERSIONS & TIPS
# ============================================

print("\n" + "=" * 60)
print("ADVANCED CONVERSIONS & PRACTICAL EXAMPLES")
print("=" * 60)

# Chain conversions
original = "12345"
chain_convert = list(set(original))
print(f"list(set('{original}')) = {chain_convert}")
print("  → String → Set (unique chars) → List")

# Boolean evaluation of collections
print("\n📊 Boolean evaluation of collections:")
print(f"  bool([]) = {bool([])}  → Empty collections are False")
print(f"  bool([1]) = {bool([1])}  → Non-empty collections are True")
print(f"  bool({{}}) = {bool({})}  → Empty dict is False")
print(f"  bool({{1}}) = {bool({1})}  → Non-empty set is True")

# Practical example: Remove duplicates while preserving order
def remove_duplicates_preserve_order(lst):
    """Remove duplicates while preserving order using dict.fromkeys()"""
    return list(dict.fromkeys(lst))

original_list = [3, 1, 2, 1, 3, 2, 4]
deduped = remove_duplicates_preserve_order(original_list)
print(f"\nPreserving order while removing duplicates:")
print(f"  Original: {original_list}")
print(f"  Deduped:  {deduped}")
print("  → dict.fromkeys() preserves first occurrence order")

# ============================================
# SUMMARY TABLE
# ============================================

print("\n" + "=" * 60)
print("CONVERSION COMPATIBILITY SUMMARY")
print("=" * 60)
print("""
From → To    | int | float | tuple | list | set | dict
-------------|-----|-------|-------|------|-----|------
int          | ✓   | ✓     | ✗¹    | ✗¹   | ✗¹  | ✗
float        | ✓²  | ✓     | ✗¹    | ✗¹   | ✗¹  | ✗
string       | ✓³  | ✓³    | ✓⁴    | ✓⁴   | ✓⁴  | ✗
bool         | ✓   | ✓     | ✗¹    | ✗¹   | ✗¹  | ✗
list         | ✗   | ✗     | ✓     | ✓    | ✓   | ✓⁵
tuple        | ✗   | ✗     | ✓     | ✓    | ✓   | ✓⁵
set          | ✗   | ✗     | ✓     | ✓    | ✓   | ✗
dict         | ✗   | ✗     | ✓⁶    | ✓⁶   | ✓⁶  | ✓

Notes:
¹ Must wrap in iterable first: tuple([x]), list([x]), set([x])
² Truncates decimal part
³ Only works with numeric strings
⁴ Each character becomes an element
⁵ Elements must be (key, value) pairs
⁶ Only keys are converted by default
""")

print("\n🔑 KEY TAKEAWAYS:")
print("• int() and float() only work with numbers, numeric strings, and bools")
print("• tuple(), list(), set() work with any iterable")
print("• dict() requires pairs of (key, value)")
print("• set() removes duplicates and loses order")
print("• dict keys are converted when converting dict to other types")
print("• Empty collections evaluate to False, non-empty to True")


'''
Claude AI:
I'll create a comprehensive Python code that demonstrates type conversion between different data types. This will be an excellent learning resource for understanding Python's type system.I've created a comprehensive Python script that demonstrates type conversion between all major Python data types. This educational code covers:

## Key Features:

1. **Complete Coverage**: Tests conversions between int, float, string, bool, tuple, list, set, and dict types

2. **Clear Explanations**: Each conversion includes comments explaining:
   - What happens during the conversion
   - Why it works (or doesn't work)
   - Special cases and gotchas

3. **Practical Examples**: 
   - Shows what conversions are possible
   - Demonstrates error cases that don't work
   - Includes real-world use cases like removing duplicates

## Important Concepts Highlighted:

- **int()** and **float()** only work with numbers, numeric strings, and booleans
- **Collections to collections** usually work (list→tuple, tuple→set, etc.)
- **set()** automatically removes duplicates and doesn't preserve order
- **dict()** requires pairs of values (like tuples of length 2)
- When converting a dictionary to other types, only the **keys** are used by default
- Single values (int, float) cannot be directly converted to collections—they must be wrapped first

## Learning Points:

The code demonstrates important Python behaviors:
- Type truncation (float to int loses decimals)
- String iteration (strings become individual characters in collections)
- Boolean evaluation of collections (empty = False, non-empty = True)
- Duplicate handling with sets
- Order preservation vs. non-preservation

Run this code to see exactly how Python handles each type conversion, complete with examples of what works, what doesn't, and why. This will give you a solid understanding of Python's type system!
'''