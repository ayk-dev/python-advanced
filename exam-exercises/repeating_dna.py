def get_repeating_DNA(string):
    i = 0
    substrings = []
    while i + 10 <= len(string):
        s = string[i:10 + i]
        substrings.append(s)
        i += 1

    repeating_strings = []
    for s in substrings:
        if substrings.count(s) > 1 and s not in repeating_strings:
            repeating_strings.append(s)

    return repeating_strings


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)
test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)
test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)