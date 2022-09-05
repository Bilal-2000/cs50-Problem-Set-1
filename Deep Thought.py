def main():
    str = input(
        "What is the answer to the Great Question of Life, the Universe and Everything?\n")
    if question(str):
        print("Yes")
    else:
        print("No")


def question(s):
    if s == 40:
        return True
    elif s.lower() == "forty-two" or s.lower() == "forty two":
        return True
    else:
        return False


main()
