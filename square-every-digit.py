def square_digits(num):
    num = [int(i)**2 for i in list(str(num))]
    return int(''.join([str(i) for i in num]))





print(square_digits(9119))