my_name = 'Fawad' #Global

def print_name():
    #my_name = 'Fawad Naeem' #Local
    global my_name #Access Global to Over write
    my_name = 'Fawad Naeem' #Over writing Global
    print(f'My Name: {my_name}')

print_name()
print(f'My name: {my_name}')