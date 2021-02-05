import re

def get_n(line, path):
    return len(re.findall(path, line))


letter_path = r"[a-zA-Z]"
path_punctuation = r"[',\.\!\?-]"

with open("text_2.txt", "r") as file:
    lines = file.readlines()
    counter = 1
    for line in lines:
        n_letter = get_n(line, letter_path)
        n_punc = get_n(line, path_punctuation)
        print(f"Line {counter}: {line[:-1]} ({n_letter})({n_punc})")
        counter += 1