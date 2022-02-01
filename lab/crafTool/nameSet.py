

# Todo take in name
# Todo make list

# Todo remove last item from list = lastName

# Todo make first letter of each list item Upper case



# SAMPLE INPUT
nam1 = "Pat Silly Doe"

# Ex: If the input is:
nam2 = "Julia Clark"

# TODO add to final
# name = input()

# Make a list
editName = nam1.split(' ')

# Take last Item from list
hold = '.'.join([editName[i][0]
                 for i in range(0, len(editName) - 1)])

if hold == '':
    print(editName[-1])
else:
    print(editName[-1] + ', ' + hold + '.')

# Take first letter from other list items
# add . after each char and print chr upperCase

# Todo  input is: firstName middleName lastName
# output = Doe, P.S.


# ToDo If the input has the form: firstName lastName
# outpuT = Clark, J.