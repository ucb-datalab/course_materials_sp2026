import fire

def hello(count, name):
    "number of greetings"
    for x in range(count):
        print('Hello, %s!' % name)

if __name__ == '__main__':
    fire.Fire(hello)
