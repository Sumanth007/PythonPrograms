def build_shift_table(pattern):
    shift_table = {}
    m = len(pattern)
    for i in range(m - 1):
        shift_table[pattern[i]] = m - 1 - i
    return shift_table


def horspool_search(text, pattern):
    m = len(pattern)
    n = len(text)
    shift_table = build_shift_table(pattern)
    shift = 0

    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            print("Pattern found at index:", shift)
            shift += shift_table.get(text[shift + m - 1], m)
        else:
            shift += shift_table.get(text[shift + m - 1], m)


text = "An Apple A Day Keeps The Doctor Away"
pattern = "Away"
horspool_search(text, pattern)
