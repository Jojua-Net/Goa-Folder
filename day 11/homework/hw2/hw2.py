


def string_clean(s):
    """
    Function will return the cleaned string
    """
    
    s_new = ""
    for i in s:
        if type(i) != str: pass
        elif i == ('@') or ('$') or ('&'): pass
        elif type(i) == str: s_new += i
        
        
    if s_new == "": return ""