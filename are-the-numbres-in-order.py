import functools


def in_asc_order(arr):
    # random_ is not allowed

    bool = arr == sorted(arr)
    #functools.reduce(lambda x,y: x and y, map(lambda p,q: p==q,sorted(arr, reverse=False),arr),True)


    return bool #(True or false)



print(in_asc_order([1,2,3,4]))