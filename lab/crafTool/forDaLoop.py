# =================================================================

# ------ Normal for loop


# daily_revenues = [
#     2356.23,  # Monday
#     1800.12,  # Tuesday
#     1792.50,  # Wednesday
#     2058.10,  # Thursday
#     1988.00,  # Friday
#     2002.99,  # Saturday
#     1890.75   # Sunday
# ]
#
# total = 0
# for day in daily_revenues:
#     total += day
#
# average = total / len(daily_revenues)
#
# print('Weekly revenue: ${:.2f}'.format(total))
# print('Daily average revenue: ${:.2f}'.format(average))

# =================================================================
# Reversed Loops

# names = [
#     'Biffle',
#     'Bowyer',
#     'Busch',
#     'Gordon',
#     'Patrick'
# ]
# for name in names:
#     print(name, '|', end=' ')
# print('\nPrinting in reverse:')
# #---
# for name in reversed(names):
#     print(name, '|', end=' ')

#
# temperatures = [30, 20, 2, -5, -15, -8, -1, 0, 5, 35]
# num_neg = 0
# for temp in temperatures:
#     if temp < 0:
#         num_neg += 1
# print(num_neg)

# =================================================================
#Fixme
#
# contact_emails = {
#     'Sue Reyn' : 's.reyn@email.com',
#     'Mike Filt': 'mike.filt@bmail.com',
#     'Nate Arty': 'narty042@nmail.com'
# }
#
# new_contact = "Mark"
# new_email = "email"
# contact_emails[new_contact] = new_email
#
# for contact_emails in reversed(contact_emails):
#     print(new_email, 'is', new_contact)



for i in range(0, -2, -1):
    print(i, end=' ')