text = input()
symbols = {}

for char in text:
    if char not in symbols:
        symbols[char] = text.count(char)
    else:
        pass

for key, value in sorted(symbols.items()):
    print(f"{key}: {value} time/s")