data = input().split()

avg_num = 0
big_num = None

for num in data:
    num = int(num)
    avg_num += num
    if big_num is None or num > big_num:
        big_num = num
print(avg_num // len(data), big_num)