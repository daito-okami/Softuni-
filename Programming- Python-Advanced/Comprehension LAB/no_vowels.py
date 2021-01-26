text = input()
vowels = {'a', 'o', 'u', 'e', 'i'}
result = [ch for ch in text if ch not in vowels]
print(''.join(result))