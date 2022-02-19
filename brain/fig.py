def recur_fib(n):
    if n <= 1:
        return n
    else:
        return(recur_fib(n - 1) + recur_fib(n - 2))

def maker_fib():
    nterms = input('Enter your positive int: ')

    # Now Check if the num of terms is valid
    if nterms <= 0:
        print('Please enter a positive int: \n')
    else:
        print('Fibonacci sequence:')
        for i in range(nterms):
            print(recur_fib(i))

if __name__ == '__main__':
    maker_fib()

