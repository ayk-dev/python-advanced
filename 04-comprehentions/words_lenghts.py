
words_lengths = {word: len(word) for word in input().split(', ')}

print(', '.join([f'{k} -> {v}' for k, v in words_lengths.items()]))

