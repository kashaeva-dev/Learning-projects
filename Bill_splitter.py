import random

print('Enter the number of friends joining (including you):')
friends_number = int(input())
friends_names = []
if friends_number <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(friends_number):
        friends_names.append(input())
    print('Enter the total bill value:')
    bill_value = float(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    if choice == 'Yes':
        lucky_name = random.choice(friends_names)
        print(f'{lucky_name} is the lucky one!')
        value = round((bill_value / (friends_number - 1)), 2)
        friends_dict = dict.fromkeys(friends_names, value)
        friends_dict.update({lucky_name: 0})
    else:
        print('No one is going to be lucky')
        pays_number = friends_number
        value = round((bill_value / friends_number), 2)
        friends_dict = dict.fromkeys(friends_names, value)
    print(friends_dict)