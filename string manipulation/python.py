import random
from tkinter.font import names

def select_raandom():
    user_input = int(input('enter how many numbers?'))
    test_list = ['fawad', 'saad', 'hammad', 'jawad', 'naeem']
    random_number = []
    for i in range(0, user_input):
        random_num = random.choice(test_list)
        random_number.append(random_num)
    for i in random_number:
        print(i)
# select_raandom()

def get_names(file_name):
    file1 = open(file_name,"r").read().replace('\n','+').split('+')
    names = []
    i = 0
    while i < len(file1):
        record = file1[i].split(',')
        names.append(record[1])
        i += 1
    return names
def show_reslts(first_file, second_file):    
    names1 = set(get_names(first_file))
    names2 = set(get_names(second_file))
    result = names1.intersection(names2)
    isEmpty = (len(result) == 0)
    if isEmpty:
        print("No common names Found")
    else:
        for i in result:
            print(i)
# first_file = input('Enter First file name')
# second_file = input('Enter second file name')
# show_reslts(first_file, second_file)