def swap_values(user_val1, user_val2):
    swap = user_val1
    user_val1 = user_val2
    user_val2 = swap
    return user_val1,user_val2

if __name__ == '__main__':
    user_val1 = int(input())
    user_val2 = int(input())

    user_val1, user_val2 = swap_values(user_val1, user_val2)

    print(user_val1, user_val2)