
def words():
    mee = 'automobile car manufacturer maker children kids'
    search_replace = []
    new = search_replace.append(mee)
    print(new)



def words_to_swap():
    a, b, c = ('automobile car', 'manufacturer maker', 'children kids')
    print(a)

    swap = [item for item in a.split()]
    swap2 = [item for item in b.split()]
    swap3 = [item for item in c.split()]



    main_sent = 'The automobile manufacturer recommends car seats for ' \
                'children if the automobile doesn\'t already have one.'


    p1 = main_sent.replace(swap[0], swap[1])
    p2 = p1.replace(swap2[0], swap2[1])
    p3 = p2.replace(swap3[0], swap3[1])
    print(p3)



  # - Expected OutPut
# The car maker recommends car seats for kids if the car doesn't already have one.


if __name__ == "__main__":

    words()
    words_to_swap()