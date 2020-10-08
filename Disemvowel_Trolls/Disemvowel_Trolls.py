def disemvowel(string):
    boin = ["a","i","u","e","o","A","I","U","E","O"]
    for i in boin:
        string = string.replace(str(i),"")
    return string
