def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if sq%sq**(0.5)==0:
        return int(((sq**0.5)+1)**2)
    else: 
        return -1



print(find_next_square(114
))