def fun(Lis):
    res = []
    for i in Lis:
        if type(i) is int:
            res.append(i)
        else:
            res += fun(i)
    return res

x = [[1, 2, [3]], 4]
print(fun(x))