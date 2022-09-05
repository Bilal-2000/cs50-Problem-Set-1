def main():
    str = input("Greeting: ")
    new = pre_process(str)
    if new.startswith('h'):
        if "hello" in new:
            print("$0")
        else:
            print("$20")
    else:
        print("$100")


def pre_process(s):
    temp = s.strip().lower()
    return temp


main()
