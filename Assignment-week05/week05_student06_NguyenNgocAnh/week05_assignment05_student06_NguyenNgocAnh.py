def inf_loop_while():
    while True:
        yield


def inf_loop_for():
    for i in inf_loop_while():
        yield