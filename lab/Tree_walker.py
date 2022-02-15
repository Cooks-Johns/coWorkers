import os

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
    path = os.path.join('lab', year)
    print()

    for dirname, subdirs, files in os.walk(path):
        print('{} will contain subdirectories: {}'.format(dirname, subdirs, end=''))
        print('and the files: {}'.format(files))


Tree_walker()


if __name__ == '__main__':
    pass

