def nb_dig(n, d):
    # your code
    result = []
    to_squares = range(0,n,1)
    for i in range(len(to_squares)):
        to_squares[i] = to_squares[i]*to_squares[i]


print(nb_dig(10,1))