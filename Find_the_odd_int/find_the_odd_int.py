def find_it(seq):
    counter = 0
    for s1 in seq:
        for s2 in seq:
            if s1 == s2:
               counter += 1
        if counter % 2 != 0:
            return s1
        counter = 0

# BestPractices
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
