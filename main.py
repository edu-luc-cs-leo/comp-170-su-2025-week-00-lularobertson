#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name, is not a valid name in python since it starts with a number.
3. age, is a valid name in python because it is descriptive.
4. total_amount, is a valid name. it is both descriptive and uses the "_" instead of a space.
5. while, is not a valid name in python because it is a "reserved" word.
6. Student, is valid because it starts with a letter and contains no special characters.
7. my-variable, is not valid because it contains a special characters "-".
8. for, is not a valid name because it is a reserved word.
9. _temp, is valid since it starts with either a letter, number, or underscore.
10. value#, is not a valid name because it contains a special character.


"""
# Problem 2
"""
1. calculate_total is a valid name since it is written in "snake case" and is descriptive.
2. 3rd_function is not valid because it starts with a number and is non descriptive.
3. print_values is valid because it is descriptive, and "print" is not a reserved word.
4. find-item is not a valid name because the hyphen is a special character, and python function names cannot contain them.
5. def is not a valid name since it is a reserved word.
6. updateProfile is a valid name, but unconventional since most names are written in snake case.
7. my_function is a valid name, but not good because it is not very descriptive and can be condusing.
8. try is a valid function name, but again seems nondescript and could be confusing.
9. init_data is a valid function name because it is written in snake case.
10. value@function is not a valid name because it contains a special character.

"""
# Problem 3
"""
1. True and False: False. A true statement and a false statement make a false statement.
2. 5 > 3 or "apple" < "banana": True. 5 > 3 is true, and "apple" has less characters than "banana" so that is true too.
    true or true is a true statement.
3. not 10 <= 20. False. 10 <= 20 is true, and then the "not" negates that so the statement is false.
4. True or 5 = 4: Not valid. The equals sign is for assigning not comparing. Should use "==" to compare instead.
5. "apple" != "orange" and 5: Not valid. "apple" != "orange" is true because the words do not contain the same
    number of characters, but 5 cannot be true or false.
6. 3 < 5 not True: Not valid. There is no logical operator in between the two parts.
7. False == (3 < 4): True. 3 < 4 is false, and false is the same as false, so the statement is true.
8. 10 <= "10": Not valid. You can't compare two different data types like integers and strings.
9. True or not False: True. not False is true, and true is true, thus the statement is true.
10. 5 and or 4: Not valid. There are two logical operators.


"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
