with open('files/write.txt','w') as write_file:
    write_file.write('Hello Fawad')
with open('files/write.txt','a') as write_file:
    write_file.write('\nHello Fawad')
name = [
    '\nCH',
    '\nFawad',
    '\nNaeem'
]
with open('files/write.txt','a') as write_file:
    write_file.writelines(name)