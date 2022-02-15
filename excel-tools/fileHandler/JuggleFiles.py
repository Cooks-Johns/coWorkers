import os
import struct


# Read file contents
# def make():
#     print('Reading in data...')
#     f = open('mydata.txt')
#     lines = f.readlines()
#     f.close()
#
#     # Iterate over each line
#     print('\nCalculating average...')
#     total = 0
#     for ln in lines:
#         total += int(ln)
#
#     # Compute result
#     avg = total/len(lines)
#     print('Average value:', avg)
#     pass

""" ------  This is will create a file.  ------"""
# with open('myfile.txt', 'w') as f:


# with open('myfile.txt', 'r') as rf:           # Reading file
#     with open('myfile.txt', 'w') as wf:  # Writing file
#         for line in rf:
#             print(line, end='4')
#             wf.write(line)
#


# ------ Flush:
# --- used to force the interpreter to flush the output buffer to disk


# with open('myfile.txt', 'w') as ff:
#
#     # No newline character, so not written to disk immediately
#     ff.write('Write me to a file, please!')
#
#     #Force output buffer to be written to disk
#     ff.flush()
#     os.fsync(ff.fileno())
#

#  os.path.join() used for creating a string for protable file
# current_day = datetime.date(1988, 6, 26)
#
# number_days = 30
# for i in range(number_days):
#     year = str(current_day.year)
#     month = str(current_day.month)
#     day = str(current_day.day)
#
#     # now set path for string
#     file_path = os.path.join('logs: {}, {}, {} log.txt'.format(year, month, day))
#
#     with open(file_path, 'r') as f:
#         print('{}: {}'.format(file_path, f.read()))
#
#     current_day = current_day + datetime.timedelta(days=1)

# urr_day = datetime.date(1997, 8, 29)
#
# num_days = 30
# for i in range(num_days):
#     year = str(curr_day.year)
#     month = str(curr_day.month)
#     day = str(curr_day.day)
#
#     # Build path string using current OS path separator
#     file_path = os.path.join('logs', year, month, day, 'myfile.txt')
#
#     f = open(file_path, 'r')
#     print('{}: {}'.format(file_path, f.read()))
#     f.close()
#
#     curr_day = curr_day + datetime.timedelta(days=1)
#
# ------------------ file paths

# p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
# print(os.path.split(p))

# ---- Search for file in dir
def File_finder():

    find_me = input(
        "Enter the file location in the following format - \n'"
        "''C:\\', 'Users', 'BWayne', 'batsuit.jpg'\n")
    p = os.path.join(find_me)
    if os.path.exists(p):
        print('Suit up... here is the path,\n {}'.format(p))

    else:
        p = os.path.join(find_me)
        print('Nothing found at\n'
              '----------------\n'
              '{}'.format(p))
    pass


#
# p = os.path.getsize('C:\\Program Files\\')
# print(os.path.split(p))

# -----------

'''# ---- This will work Walk a dir tree like this one below


logs/
    2009/      
        April/
                1/
                 log.txt
                 words.doc                                     
        January/
               15/
                 log.txt
               21/
                 log.txt
                 temp23.pdf
               24/
                 presentation.ppt
    2010/
        March/
             3/
              log.txt
             7/
              music.mp3
'''
def Tree_walker():
    year = input('Enter your year: \n')
    path = os.path.join('logs', year)
    print()

    for dirname, subdirs, files in os.walk(path):
        print('{} will contain subdirectories: {}'.format(dirname, subdirs, end=''))
        print('and the files: {}'.format(files))
    pass

# ==------ byte objects
def tasty_bytes():
    my_bytes = b'This is a taste of a byte literal'
    print(my_bytes)
    print(type(my_bytes))
    pass

# -----------
def byte_string_literal():
    print(b'123456789 @ is the same as \x31 \x32 \x33 \x34 \x35 \x36 \x37 \x38 \x39 \x40')
    pass

# ----------- This will read the binary data fo a image
def read_image_binary():
    with open('dingonek.PNG', 'rb') as f:
        contents = f.read()
        print('Contents of ball.bmp:\n')
        print(contents)
    pass


# # --------- Todo Look into wy this isn't working as expected
# def baller():
#     ball_file = open('ball.bmp', 'rb')
#     ball_data = ball_file.read()
#     ball_file.close()
#
#     # BMP image file format stores location
#     # of pixel RGB values in bytes 10-14
#     pixel_data_loc = ball_data[10:14]
#
#     # Converts byte sequence into integer object
#     pixel_data_loc = struct.unpack('<L', pixel_data_loc)[0]
#
#     # Create sequence of 3000 red, green, and yellow pixels each
#     new_pixels = b'\x01'*3000 + b'\x02'*3000 + b'\x03'*3000
#
#     # Overwrite pixels in image with new pixels
#     new_ball_data = ball_data[:pixel_data_loc] + \
#                   new_pixels + \
#                   ball_data[pixel_data_loc + len(new_pixels):]
#
#     # Write new image
#     new_ball_file = open('new_ball.bmp', 'wb')
#     new_ball_file.write(new_ball_data)
#     new_ball_file.close()
#

## ----- Packing values
def packing_values():
    print('Result of packing 65231235:', end=' ')
    print(struct.pack('>h', 3276))

    print('Result of packing 5,234, 9243:', end=' ')
    print(struct.pack('>hhh', 5, 234, 9243))

    print('Result of packing 1235:', end=' ')
    print(struct.pack('>h', 1235))


    print('Result of packing 5 and 256 and 455:', end=' ')
    print(struct.pack('>hhh', 5, 256, 455))


## ----- Un-Packing values
def unpacking_byte():
    print('Result of unpacking {}:'.format(repr('\x00\x05')), end=' ')
    print(struct.unpack('>h', b'\x00\x05'))

    print('Result of unpacking {}:'.format(repr('\x01\x00')), end=' ')
    print(struct.unpack('>h', b'\x01\x00'))

    print('Result of unpacking {}:'.format(repr('\x00\x05\x01\x00')), end=' ')
    print(struct.unpack('>hh', b'\x00\x05\x01\x00'))



if __name__ == '__main__':
    pass

