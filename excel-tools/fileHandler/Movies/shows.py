def readFile(filename):

   dict = {}

   with open(filename, 'r') as infile:

       lines = infile.readlines()

       for index in range(0, len(lines) - 1, 2):

           if lines[index].strip()=='':continue

           count = int(lines[index].strip())

           name = lines[index + 1].strip()

           if count in dict.keys():

               name_list = dict.get(count)

               name_list.append(name)

               name_list.sort()

           else:

               dict[count] = [name]

           print(count,name)

   return dict

def output_keys(dict, filename):

   with open(filename,'w+') as outfile:

       for key in sorted(dict.keys()):

           outfile.write('{}: {}\n'.format(key,';'.join(dict.get(key))))

           print('{}: {}\n'.format(key,';'.join(dict.get(key))))

def output_titles(dict, filename):

   titles = []

   for title in dict.values():

       titles.extend(title)

   with open(filename,'w+') as outfile:

       for title in sorted(titles):

           outfile.write('{}\n'.format(title))

           print(title)

def main():

   filename = input('Enter input file name: ')

   dict = readFile(filename)

   if dict is None:

       print('Error: Invalid file name provided: {}'.format(filename))

       return

   print(dict)

   output_filename_1 ='output_keys.txt'

   output_filename_2 ='output_titles.txt'

   output_keys(dict,output_filename_1)

   output_titles(dict,output_filename_2)

main()