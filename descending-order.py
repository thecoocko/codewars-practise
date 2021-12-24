def descending_order(num):

    num = list(str(num))

    for i in range(len(num)):
        num[i]=int(num[i])

    num = sorted(num,reverse=True)
    return ''.join([str(i) for i in num])



print(descending_order(1234567))