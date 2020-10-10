def get_middle(s):
    #your code here
    i = (len(s)-1) // 2
    s_len = len(s)
    if s_len % 2 == 0:
        return(s[i:i+2])
    else:
        return(s[i])
