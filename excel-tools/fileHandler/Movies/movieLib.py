'''

---- output_keys.txt

10: Will & Grace
12: Murder, She Wrote
14: Dallas
20: Gunsmoke; Law & Order
30: The Simpsons

'''

# FIXME -- need to remove the first line from the file
    # TODO -- Learn why the first line is printing they way it is

# file.readlines()

def main(filename):
    with open(filename) as file:  # open file
        data = file.readlines()
    dict_info = {}
    for i in range(0, len(data) - 1, 2):
        season = data[i].strip()
        name = data[i + 1].strip()
        if (season in dict_info):
            dict_info[season].append(name)
        else:
            dict_info[season] = [name]



    # OUTPUT KEYS
    keys = list(dict_info.keys())  # will list the dictionary keys
    keys.sort()  # will sort the keys from min to max
    with open('output_keys.txt', 'w') as file:
        for key in keys:
            names = '; '.join(name for name in dict_info[key])  # will print the name with number
            file.write(str(key) + ': {}\n'.format(names))
    names = []  # Dictionary value
    for item in dict_info:  # will add name to dict
        for name in dict_info[item]:
            names.append(name)



            # OUTPUT TITTLE
    names.sort()  # sort names from min to max
    with open('output_titles.txt', 'w') as file:  # open the file
        for name in names:  # will write name plus a new line
            file.write(name + '\n')





def readFile(filename):

    with open(filename, 'r') as file:
        c = file.readlines()
        s = c.items()
        print(s)





# seasons = keys
# tv_shoes = values



# Driver code
# readFile('movie-list')


main('movie-list')


'''
---- output_titles.txt

Dallas
Gunsmoke
Law & Order
Murder, She Wrote
The Simpsons
Will & Grace

'''

