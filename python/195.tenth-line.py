with open("file.txt") as f:
    try:
        print(f.readlines()[9])
    except IndexError:
        print("")
