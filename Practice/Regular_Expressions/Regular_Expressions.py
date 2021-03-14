import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

#Phone number match from data.txt
#pattren = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
#pattren = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
pattren = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
with open('data.txt','r') as f:
    contents = f.read()
    #matches = pattren.finditer(contents)
    matches = pattren.finditer(text_to_search)
    for match in matches:
        print(match)
   


