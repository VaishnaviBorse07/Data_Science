# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 19:25:44 2025

@author: vaish
"""

# 1. Reverse the order of list
def reverse_list(lst):
    return lst[::-1]

# 2. Check number of occurrences of specified elements in the list
def count_occurrences(lst, elem):
    return lst.count(elem)

# 3. Append list1 with list2 in the front
def append_lists_front(list1, list2):
    return list2 + list1

# 4. Insert new item before the second element
def insert_before_second(lst, item):
    if len(lst) > 1:
        lst.insert(1, item)
    return lst

# 5. Remove first occurrence of specified element
def remove_first_occurrence(lst, elem):
    if elem in lst:
        lst.remove(elem)
    return lst

# 6. Check whether an element exists in a tuple
def element_exists(tpl, elem):
    return elem in tpl

# 7. Replace last value of each tuple in list to 100
def replace_last_value(lst):
    return [t[:-1] + (100,) for t in lst]

# 8. Add a key and value in the dictionary
def add_key_value(dct, key, value):
    dct[key] = value
    return dct

# 9. Concatenate dictionaries
def concatenate_dicts(d1, d2):
    d1.update(d2)
    return d1

# 10. Create dictionary where keys are from 1 to 15 and values are their squares
def create_square_dict():
    return {i: i**2 for i in range(1, 16)}

# 11. Sum of all values in a dictionary
def sum_dict_values(dct):
    return sum(dct.values())

# Example usage
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print("Reversed List:", reverse_list(lst))
    
    lst2 = [1, 2, 3, 1, 4, 1]
    print("Occurrences of 1:", count_occurrences(lst2, 1))

    list1 = [4, 5, 6]
    list2 = [1, 2, 3]
    print("Appended List:", append_lists_front(list1, list2))

    lst3 = [10, 20, 30]
    print("After Inserting:", insert_before_second(lst3, 15))

    print("After Removing First Occurrence:", remove_first_occurrence(lst2, 1))

    tpl = (1, 2, 3, 4)
    print("Element Exists:", element_exists(tpl, 3))

    tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    print("Modified Tuples:", replace_last_value(tuples_list))

    dct = {"a": 1, "b": 2}
    print("Updated Dictionary:", add_key_value(dct, "c", 3))

    d1 = {1: "A", 2: "B"}
    d2 = {3: "C", 4: "D"}
    print("Concatenated Dictionary:", concatenate_dicts(d1, d2))

    print("Square Dictionary:", create_square_dict())

    dct_values = {"a": 10, "b": 20, "c": 30}
    print("Sum of Dictionary Values:", sum_dict_values(dct_values))
