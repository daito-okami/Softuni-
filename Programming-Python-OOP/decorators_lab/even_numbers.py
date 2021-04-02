def even_numbers(func):
    def wrapper(numbers):
        result = func(numbers)
        return [x for x in result if x % 2 == 0]

    return wrapper
