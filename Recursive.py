# Practice 1: Sum individual digits

def sum_digits(n):
  # Base case:
  if n <= 9:
    return n

  # Recursive step:
  last_digit = n % 10
  return(sum_digits(n // 10)) + last_digit


# test cases

print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)

# Practice 2: Find minimum value

def find_min(my_list):

  # Base case
  if len(my_list) == 0:
    return None
  if len(my_list) == 1:
    return my_list[0]

  temp = my_list[0] if my_list[0] < my_list[1] else my_list[1]
  my_list[1] = temp
  return find_min(my_list[1:])


# test cases
print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)

# Practice 3: Check for palindromes
string = "racecar"

def is_palindrome(my_string):
  if len(my_string) < 2:
    return True
  if my_string[0] != my_string[-1]:
    return False
  return is_palindrome(my_string[1:-1])

# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)


# Practice 4: Mutliplication

def multiplication(num1, num2):

  if num1 == 0 or num2 ==0:
    return 0
  return num1 + multiplication(num1, (num2 - 1))


# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)