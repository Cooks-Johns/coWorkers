#
#
# # SAMPLE INPUT
# # Pat Silly Doe
#
# # Ex: If the input is:
# # Julia Clark
#
# nam1 = "Pat Silly Doe"
# nam2 = "Julia Clark"
#
# # Make a list
# name = input("Enter number of elements : ").split()
#
#
#
# # Below line read inputs from user using map() function
#
# print("\nList is - ", name)
#
#
# # Take last Item from list
# # Take first letter from other list items
# # add . after each char and print chr upperCase
#
#
# print('')
#
# # Todo  input is: firstName middleName lastName
# # output = Doe, P.S.
#
#
# # ToDo If the input has the form: firstName lastName
# # outpuT =

#
# def name(s):
#     # split the string into a list
#     l = s.split()
#     new = ""

    # traverse in the list
    # for i in range(len(l) - 1):
    #     s = l[i]
    #
    #     # adds the capital first character
    #     new += (s[0].upper() + '.')
    #
    # # l[-1] gives last item of list l. We
    # # use title to print first character in
    # # capital.
    # new += l[-1].title()

    #
    # return new


# Driver code
s = "Pat Silly Doe"

split = s.split()
q = len(split)


print(q)
name = ''
if q == 3:
    lasname = split[2].title()
    firname = split[0].upper()
    midname = split[1].upper()
    name = "{}, {}.{}.".format(lasname, firname[0], midname[0])
    print(name)
else:
    lasname = split[1].title()
    firname = split[0].upper()
    name = "{}, {}.".format(lasname, firname[0])
    print(name)

