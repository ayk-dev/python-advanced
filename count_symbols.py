text = tuple(input())

unique_symbols = sorted(set(text))
for symbol in unique_symbols:
    counts = text.count(symbol)
    print(f'{symbol}: {counts} time/s')
