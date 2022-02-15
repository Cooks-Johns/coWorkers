import csv
'''
,,,,final
,9,8,85,78
Sam Tarley,10,10,99,100
Joff King,4,2,55,61

'''

def write_csv():
    row = ['name', 'hw1', 'hw2', 'midterm', 'final']
    row1 = ['Petr Little', '9', '8', '85', '78']
    row2 = ['Sam Tarley', '10', '10', '99', '100']
    row3 = ['Joff King', '4', '2', '55', '61']

    with open('grades.csv', 'w') as csvfile:
        write_grades = csv.writer(csvfile)

        write_grades.writerow(row)
        write_grades.writerow(row1)
        write_grades.writerow(row2)
        write_grades.writerow(row3)


        write_grades.writerow([row, row2])



def read_csv():
    g = input('Enter csv name: \n')
    with open(g, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        row_num = 1
        for row in csv_reader:
            print('Row #{}:'.format(row_num), row)
            row_num += 1
    pass
# --------------

def calculat_csv():
    # Dictionary that maps student names to a list of scores
    grades = {}

    # Use with statement to guarantee file closure
    with open('grades.csv', 'r') as csvfile:
        grades_reader = csv.reader(csvfile, delimiter=',')

        first_row = True
        for row in grades_reader:
            # Skip the first row with column names
            if first_row:
                first_row = False
                continue

            ## Calculate final student grade ##
            # FIXME
            '''calculat_csv
                            name = row[1]
            IndexError: list index out of range'''
            name = row[0]

            # Convert score strings into floats
            scores = [float(cell) for cell in row[1:]]

            hw1_weighted = scores[0] / 10 * 0.05
            hw2_weighted = scores[1] / 10 * 0.05
            mid_weighted = scores[2] / 100 * 0.40
            fin_weighted = scores[3] / 100 * 0.50

            grades[name] = (hw1_weighted + hw2_weighted +
                            mid_weighted + fin_weighted) * 100

    for student, score in grades.items():
        print('{} earned {:.1f}%'.format(student, score))


if __name__ == '__main__':
    calculat_csv()