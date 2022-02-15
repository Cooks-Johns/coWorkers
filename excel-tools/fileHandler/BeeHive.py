
# File searching

# f = open('working.txt', 'r')
#
# print(f.mode)
# f.close()
#  ---------------

# with open('working.txt', 'r') as f:
#     f_contents = f.read()
#     print(f_contents)

# ---------------  reading file but the code is reapeating

# with open('working.txt', 'r') as f:
#     f_contents = f.readline()
#     print(f_contents, end='') # ad end='' to remove space

    # f_contents = f.readline()
#     print(f_contents, end='') # ad end='' to remove space

# #  ---------------  for loops stops repeating code
#
# with open('working.txt', 'r') as f:
#
#     for line in f: # by adding the for loop you can parse the file without
#         print(line, end='')

#  ---------------  using vars to pick how much of the file you want to read

# with open('working.txt', 'r') as f:
#
#     size_to_read = 10
#
#
#
#     f.seek(100) # using seek you can choose the postion where to start again
#
#     f_contents = f.read(size_to_read)
#     print(f_contents)

#  --- for loops stops repeating code
    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read((size_to_read))

#  --------------- ----------------      Writing to file
#
# with open('lilBee.txt', 'w') as f: # running this alone will create the file
#
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

#  --------  REad a file and then copy it to a new file

# with open('working.txt', 'r') as rf:           # Reading file
#     with open('mydata.txt', 'w') as wf:  # Writing file
#         for line in rf:
#             wf.write(line)

# ------ read and copy image
# rEading images you will need to put it into binary mode
# with open('dingonek.PNG', 'rb') as rf:
#     with open('dingonek_copy.PNG', 'wb') as wf:
#         chunk_size = 4096
#         rf_chunk = rf.read(chunk_size)
#
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)


def Alter_bmp_image():

    with open('dingonek.PNG', 'rb') as working_img:

        img_data = working_img.read()
        print('Working....\n')
# Store the BMP img formate
# pixel RGB value in bytes 10-14
        pixel_data_location = img_data[10:14]

# Sequence of 3000 rgby pixels
        new_pixels = b'\x01'*3000 + b'\x02'*3000 + b'\x03'*3000

# OVerwrite pixels in img with new pixels
        new_img_data = img_data[:pixel_data_location] + \
                        new_pixels + \
                        img_data[pixel_data_location + len(new_pixels)]
# Build new image
        new_file = open('new_file.PNG', 'wb')
        new_file.write(new_img_data)
        print('Done.')


Alter_bmp_image()









if __name__ == '__main__':
    pass

