import functools
import time


def calculate_time(fn):
    @functools.wraps(fn)
    def calculate(*args):
        start = time.time()
        fn(*args)
        print(time.time() - start)
    return calculate


@calculate_time
def to_calculate(time_to_sleep):
    time.sleep(time_to_sleep)


to_calculate(1)
to_calculate(3)
