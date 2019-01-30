
def reverse_arr_str(s):
    """
    """
    # Handle Edge Case #1
    if (s == None or len(s) == 0):
        return ""

    i = 0
    j = len(s) - 1
    while i <= j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s

    # One liner solution:
    # return "".join(list(s)[::-1])


print(reverse_arr_str(["a", "b", "c", "d"]))

