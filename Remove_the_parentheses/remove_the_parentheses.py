def remove_parentheses(s):
    import re
    
    table = {"(": "（",
        ")": "）",
       }
    for key in table.keys():
        s = s.replace(key, table[key])
    l = ['（[^（|^）]*）']
    for l_ in l:
        s = re.sub(l_, "", s)
    return remove_parentheses(s) if sum([1 if re.search(l_, s) else 0 for l_ in l]) > 0 else s

import re


# https://qiita.com/mynkit/items/d6714b659a9f595bcac8
#def delete_brackets(s):
#    """
#    括弧と括弧内文字列を削除
#    """
#    """ brackets to zenkaku """
#    table = {
#        "(": "（",
#        ")": "）",
#        "<": "＜",
#        ">": "＞",
#        "{": "｛",
#        "}": "｝",
#        "[": "［",
#        "]": "］"
#    }
#    for key in table.keys():
#        s = s.replace(key, table[key])
#    """ delete zenkaku_brackets """
#    l = ['（[^（|^）]*）', '【[^【|^】]*】', '＜[^＜|^＞]*＞', '［[^［|^］]*］',
#         '「[^「|^」]*」', '｛[^｛|^｝]*｝', '〔[^〔|^〕]*〕', '〈[^〈|^〉]*〉']
#    for l_ in l:
#        s = re.sub(l_, "", s)
#    """ recursive processing """
#    return delete_brackets(s) if sum([1 if re.search(l_, s) else 0 for l_ in l]) > 0 else s