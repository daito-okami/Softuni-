n = int(input())

odd_set = set()
even_set = set()


for curr_ite in range(1, n+1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // curr_ite
    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)


sum_evens = sum(even_set)
sum_odd = sum(odd_set)

if sum_evens == sum_odd:
    modded_set = [str(el) for el in even_set.union(odd_set)]
    print(f"{', '.join(modded_set)}")
elif sum_odd > sum_evens:
    modded_set = [str(el) for el in odd_set.difference(even_set)]
    print(f"{', '.join(modded_set)}")
else:
    modded_set = [str(el) for el in even_set.symmetric_difference(odd_set)]
    print(f"{', '.join(modded_set)}")