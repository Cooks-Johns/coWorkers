The code below demonstrates use of string functions:

#  Author: Dr. Meadors
#
# Check out this site - https://www.w3schools.com/python/python_ref_string.asp
#
#

i1=5
j1=7

a1 = "Hello"
a2 = "See ya"
a3 = "lower case"
a4 = "today is today and today is also today"

a1s = a4.count("today")
print ("There are " + str(a1s) + " occurrences of the word 'today'.")

a3s = a3.capitalize()
print ("The string of '" + a3 + "' with the first letter capitalized is '" + a3s + "'.")

a1n = a1.isalnum()

print("Return either a Boolean result, that is either True or False")
print("The variable of '" + a1 + "' is a alphanumeric, True or False? " + str(a1n) + ".")