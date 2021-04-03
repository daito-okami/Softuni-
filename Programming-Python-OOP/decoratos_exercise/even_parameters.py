def even_parameters(func):
    def wrapper(*args):
        try:
            not_evens = [el for el in args if el % 2 == 0]
            if not_evens:
                raise TypeError
        except TypeError:
            return "Please use only even numbers!"
        return func(*args)
    return wrapper


