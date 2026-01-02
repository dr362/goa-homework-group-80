# Task 7: Check Even or Odd
# Instructions:
# write code that returns True if number is even, otherwise False.
# Test Cases:
# assert is_even(4) == True
# assert is_even(7) == False
# assert is_even(0) == True

def even_or_Odd(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(even_or_Odd(2))