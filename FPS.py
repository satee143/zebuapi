import time

value = 24
result = (1 / value)


def newVal():
    timer_one = time.time()
    for i in range(value):
        time.sleep(result)
    print('%s' % (time.time() - timer_one))


newVal()
