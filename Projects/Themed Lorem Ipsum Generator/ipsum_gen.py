from random import randint

words = ['fawad','hammad','saad','jawad']

def generate(word):
    random_pos = randint(0, len(words) -1)
    return f'{word} {words[random_pos]}'

paragraphs = int(input('How many paragraphs?:'))

with open('ipsum.txt') as ipsum_orignal:
    items = ipsum_orignal.read().split()
    for n in range(paragraphs):
        text = list(map(generate, items))
        with open('nin_ipsum.txt','a') as ipsum:
            ipsum.write(''.join(text) + '\n\n')