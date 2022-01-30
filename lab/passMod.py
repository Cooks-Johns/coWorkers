
word = 'myBirthday'


i = '!'
a = '@'
m = 'M'
b = '8'
o = '.'

if "o" in word:
    tokens = word.split('o')
    word = o.join(tokens)

if "i" in word:
    tokens = word.split('i')
    word = i.join(tokens)

if "a" in word:
    tokens = word.split('a')
    word = a.join(tokens)

if "m" in word:
    tokens = word.split('m')
    word = m.join(tokens)

if "B" in word:
    tokens = word.split('B')
    word = b.join(tokens)

chang_end = ''.join(word.split())
print('{}q*s'.format(chang_end))