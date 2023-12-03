def build_bad_char_table(pattern):
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    bad_char = build_bad_char_table(pattern)
    shift = 0

    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            print("Pattern found at index:", shift)
            shift += (m - bad_char.get(text[shift + m], -1))
        else:
            shift += max(1, j - bad_char.get(text[shift + j], 0))



text = """TGCACCAAACATGTCTAAAGCTGGAACCAAAATTACTTTCTTTGAAGACAAAAACTTTCAAGGCCGCCACTATGACAGCGATTGCGACTGTGCAGATTTCCACATGTACCTGAGCCGCTG

CAACTCCATCAGAGTGGAAGGAGGCACCTGGGCTGTGTATGAAAGGCCCAATTTTGCTGGGTACATGTACATCCTACCCCGGGGCGAGTATCCTGAGTACCAGCACTGGATGGGCCTCAA

CGACCGCCTCAGCTCCTGCAGGGCTGTTCACCTGTC"""
pattern = "CTGTGTATGAAA"
boyer_moore_search(text, pattern)
