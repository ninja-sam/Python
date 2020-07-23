# Program to check if a string is palindrome or not

#my_str = 'aIbohPhoBiA'
my_str = str(input("Enter a string for Palindrome Test: "))

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")