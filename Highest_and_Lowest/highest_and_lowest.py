def high_and_low(numbers):
    num =[int(number) for number in numbers.split()]
    return str(max(num)) + " " + str(min(num))
    