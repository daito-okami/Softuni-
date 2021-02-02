def even_odd(*args,):
    command = args[-1]
    if command == "even":
        return list(filter(lambda x: x % 2 == 0, args[0:-1]))
    return list(filter(lambda x: x % 2 != 0, args[0:-1]))