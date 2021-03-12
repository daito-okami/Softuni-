class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for arg in args:
            result *= arg
        return result

    @staticmethod
    def divide(initial, *args):
        result = initial
        for arg in args:
            result /= arg
        return result

    @staticmethod
    def subtract(initial, *args):
        result = initial
        for arg in args:
            result -= arg
        return result