from timeit import default_timer as timer
def exec_time(func):
    def wrapper(*args):
        start_time = timer()
        func(*args)
        end = timer() - start_time
        return end
    return wrapper
