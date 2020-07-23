# print(threading.current_thread().getName())

def display():
    for i in range(10):
        print('\thello')


t = Thread(target=display)
t.start()

for i in range(10):
    print('\thi')
