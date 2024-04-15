import sys
def main():
    print('Python.Version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)

    import random
    x = list(range(0, 30))
    print(x)
    random.shuffle(x)
    print(x)
    import datetime
    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)


if __name__=="__main__":main()