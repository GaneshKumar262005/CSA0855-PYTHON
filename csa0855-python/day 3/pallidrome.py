def is_palindrome(num_str):
if len(num_str) <= 1:
return True
if num_str[0] == num_str[-1]:
return is_palindrome(num_str[1:-1])
else:
return False
test_cases = [12321, 12345, 1221, 123454321]
for number in test_cases:
num_str = str(number)
result = f"{number} is a palindrome" if
is_palindrome(num_str) else f"{number} is not a
palindrome"
print(result)
