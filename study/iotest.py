if __name__ == '__main__':
    with open(r"C:\Users\27172\Desktop\py.txt", "r", encoding="UTF-8") as stream:
        print(stream.read())

    with open(r"C:\Users\27172\Desktop\py.txt", "r", encoding="UTF-8") as stream2:
        stream2.readlines()
