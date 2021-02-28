#ipsum_file = open('files/ipsum.txt')
# #For loop
# for line in ipsum_file:
#     print(line.rstrip()) #rstrip() removes the space between lines

# ipsum_file.seek(0) # This will move the cursor at 0th position


# lines = ipsum_file.readlines()
# print(lines)

# ipsum_file.seek(50)
# file_text = ipsum_file.read(100)
# print(file_text)

# ipsum_file.close()

def S_filter(line):
    return '>' not in line


with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    print(list (filter (S_filter, lines) ) )
