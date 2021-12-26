from collections import defaultdict


def count(string):
    # The function code should be here
    chars = defaultdict(int)
    if not string:
        return {}
    else:
        for char in string:
            chars[char] += 1
            
        return dict(chars)




print(count('aba'))