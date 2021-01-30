def cal_combinations(names, n, combs=[]):
    if len(combs) ==n:
        print(", ".join(combs))
        return
    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        cal_combinations(names[i+1:], n, combs)
        combs.pop()


names = input().split(", ")
n = int(input())
cal_combinations(names, n)