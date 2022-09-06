def main():
    name = input("Please enter the name of file: ").lower()
    print(check_Type(name))


def check_Type(n):
    if ".gif" in n:
        return "image/gif"
    elif ".jpg" in n or ".jpeg" in n:
        return "image/jpeg"
    elif ".png" in n:
        return "image/png"
    elif ".pdf" in n:
        return "application/pdf"
    elif ".txt" in n:
        return "text/plain"
    elif ".zip" in n:
        return "application/zip"
    else:
        return "application/octet-stream"


main()
