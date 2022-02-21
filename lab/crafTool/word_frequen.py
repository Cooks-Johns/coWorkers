# hey hi Mark hi mark

# Take user input
# st =  # input()
# s = st.replace(' ', ',')


# print(s)

lst2 = [item for item in 'hey hi Mark hi mark'.split()]

print(lst2)


def wordRepeat(str):
    # break the string into list of words
    string_list = str.split()

    # gives set of unique words
    # same_word = set(string_list)

    for words in string_list:
        print(words, string_list.count(words))


# driver code
if __name__ == "__main__":
    str = 'hey hi Mark hi mark'

    # calling the freq function
    wordRepeat(str)