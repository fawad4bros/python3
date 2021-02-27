#anonymous function dont need name or identifier, small function every used once
nums = [1,2,3,4,5]

def square(n):
    return n*n
print(list(map(square,nums)))
#lambda function
#lambda n: n*n
#Multiple arguments
#lambda n,x: x+n*n
print(list(map(lambda n : n*n,nums)))