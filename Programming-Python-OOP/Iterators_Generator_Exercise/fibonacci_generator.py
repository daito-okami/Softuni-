def fibonacci():
    previous_num, current_num = 0, 1
    while True:
        yield previous_num
        previous_num, current_num = current_num, previous_num + current_num