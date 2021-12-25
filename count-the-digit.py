
def nb_dig(n, d):
    # your code
    to_squares = sum([str(i**2).count(str(d)) for i in list(range(0,n+1,1))])

    return to_squares


print(nb_dig(10,1))