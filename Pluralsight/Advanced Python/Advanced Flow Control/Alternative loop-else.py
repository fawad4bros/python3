"""Alternatives to while-else and for-else"""
""" Best Practice """

def ensure_divisible(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return divisor
items = [2,25,9]
divisor = 12
divided = ensure_divisible(items, divisor)
print("{items} contains {divided} which is a multiple of {divisor}".format(**locals()))