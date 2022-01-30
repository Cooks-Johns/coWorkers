triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))

tri_spa = '{} '.format(triangle_char)

for i in range(1, triangle_height + 1):
    print(triangle_char * i)


for i in range(1, triangle_height + 1):
    stars = ''
    for star in range(1, i + 1):
        stars += tri_spa
    print(stars)