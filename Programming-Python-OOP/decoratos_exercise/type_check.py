def type_check(type_check):
    def decorator(func):
        def wrapper(param):
            if isinstance(param, type_check):
                return func(param)
            return "Bad Type"

        return wrapper
    return decorator