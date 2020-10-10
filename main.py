global index
index = 0

def do_something():
    global index
    index += 1
    print("I'm doing something, for example, adding values like this: " + str(index))

if __name__ == "__main__":
    do_something()
