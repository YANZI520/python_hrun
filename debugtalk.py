
import time


def sleep(n_secs):
    time.sleep(n_secs)


def get_phone():
    import random
    phone = "1" + random.choice(["3", "5"])
    for i in range(9):
        num = random.randint(0, 9)
        phone = phone + str(num)
    return phone


if __name__ == '__main__':
    print(get_phone())
