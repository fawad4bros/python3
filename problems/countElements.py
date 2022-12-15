
def countElements(arg):
    """
    Arg: str list
    Return: dict
    """
    data = arg
    dic = {}
    count = 0
    for i in data:
        count = data.count(i)
        dic[i] = count
    dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    return dict(dic) 