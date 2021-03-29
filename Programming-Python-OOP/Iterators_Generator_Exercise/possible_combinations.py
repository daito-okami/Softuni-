from itertools import permutations


def possible_permutations(nums):
    for el in permutations(nums):
        yield list(el)