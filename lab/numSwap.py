# one = 2
# two = 93
#
#
# def swap_values(user_val1, user_val2):
#     user_val1 = one
#     user_val2 = two
#     tmp = [user_val2, user_val1]
#     return tmp


#
# def print_val():
#
#     print('Sum: {:f}'.format(tmp))
# swap_values()
# print()
#

# ----------------->        this is how you edit the list
# def modify(my_list):
#     my_list[1] = 99 # list location my_list[1]
#
# my_list = [10, 20, 30]
# modify(my_list)
# print(my_list)

# -------------
# def modify(my_list):
#     my_list[1] = 99  # Modifying only the copy
#
# my_list = [10, 20, 30]
# modify(my_list[:])  # Pass a copy of the list
#
# print(my_list)  # my_list does not contain 99!

# -------------

# def add_grade(student_grades):
#     print('Entering grade. \n')
#     name, grade = input(grade_prompt).split()
#     student_grades[name] = grade
#
#
# def delete_name():
#     name = input(delete_prompt)
#     del student_grades[name]
#     print('Deleting grade.\n')
#
# def print_grades():
#     print('Printing grades.\n')
#     for name, grade in student_grades.items():
#         print(name, 'has a', grade)
#
#
# student_grades = {}  # Create an empty dict
# grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
# delete_prompt = "Enter name to delete:\n"
# menu_prompt = ("1. Add/modify student grade\n"
#                 "2. Delete student grade\n"
#                 "3. Print student grades\n"
#                 "4. Quit\n\n")
#
# command = input(menu_prompt).lower().strip()
#
#
# while command != '4':  # Exit when user enters '4'
#     if command == '1':
#         add_grade(student_grades)
#
#     elif command == '2':
#         delete_name()
#
#     elif command == '3':
#         print_grades()
#
#     else:
#         print('Unrecognized command.\n')
#
#     command = input().lower().strip()
# --------------------------->


def get_tmp(user_val1, user_val2, ):
    a = user_val1
    b = user_val2
    tmp = [b, a]
    # print('Sum: {}'.format(tmp, sep=','))
    return tmp

def mak_str():
    t = ' '.join(str(x) for x in td)
    print(t)

a, b = 5 , -21

td = get_tmp(a, b)

mak_str()

#------------------------->
# def split(s):
#
#     token = values_list.split(',')
#     s = token
#     print(s)
#
#
#
# # values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# values_list = 'all,good,things,must,end,here'
#
# if __name__ == '__main__':
#     split(values_list)



def swap_values(a,b):
    x = a
    y = b
    print('{} {}'.format(x, y))

b = int(input())
a = int(input())

swap_values(a,b)
