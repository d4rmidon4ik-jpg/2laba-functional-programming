import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Время: {end - start} сек")
    return wrapper

def function1():
    time.sleep(1)
    print("Функция 1")

task = timer(function1)

task()

