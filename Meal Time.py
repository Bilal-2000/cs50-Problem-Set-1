import random


def main():
    ch = int(input(
        "Please enter the format of time i.e(1 for)12-hour or (2 for)24-hour: "))
    time = (input("What time is it: ")).replace(" ", ":").split(":")
    if ch == 1:
        c = convert_12(time)
        # Numeric formatting
        print(f"{c:.1f}")
    elif ch == 2:
        c = convert_24(time)
        # Numeric formatting
        print(f"{c:.1f}")
    else:
        print("Wrong input")


def convert_24(time):
    index = 0
    time_first = (time[index])
    if time_first == '8' and time[index + 1] == "00":
        print("Breakfast time")
        return random.uniform(7, 8)
    elif int(time_first) in range(7, 8):
        print("Breakfast time")
        return random.uniform(7, 8)
    elif time_first == '13' and time[index + 1] == "00":
        print("Lunch time")
        return random.uniform(12, 13)
    elif int(time_first) in range(12, 13):
        print("Lunch time")
        return random.uniform(12, 13)
    elif time_first == '19' and time[index + 1] == "00":
        print("Dinner time")
        return random.uniform(18, 19)
    elif int(time_first) in range(18, 19):
        print("Dinner time")
        return random.uniform(18, 19)
    else:
        return 0


# The challenge function
def convert_12(time):
    index = 0
    time_first = (time[index])
    if time_first == '8' and time[index + 1] == "00" and time[index + 2] == "a.m.":
        print("Breakfast time")
        return random.uniform(7, 8)
    elif int(time_first) in range(7, 8) and time[index + 2] == "a.m.":
        print("Breakfast time")
        return random.uniform(7, 8)
    elif time_first == '1' and time[index + 1] == "00" and time[index + 2] == "p.m.":
        print("Lunch time")
        return random.uniform(12, 1)
    elif int(time_first) in range(12, 13) and time[index + 2] == "p.m.":
        print("Lunch time")
        return random.uniform(12, 1)
    elif time_first == '8' and time[index + 1] == "00" and time[index + 2] == "p.m.":
        print("Dinner time")
        return random.uniform(7, 8)
    elif int(time_first) in range(7, 8) and time[index + 2] == "p.m.":
        print("Dinner time")
        return random.uniform(7, 8)
    else:
        return 0


if __name__ == "__main__":
    main()
