def get_count(input_str):
    num_vowels = 0
    # your code here
    boin = ["a","e","i","o","u"]
    for i in boin:
        num_vowels += input_str.count(i)
    return num_vowels
