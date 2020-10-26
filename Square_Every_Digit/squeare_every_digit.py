def square_digits(num):
    s_num = ""
    for n in range(len(str(num))):
        s = int(str(num)[n]) ** 2
        s_num += str(s)
    return int(s_num)
