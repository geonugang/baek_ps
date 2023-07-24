for i in range(100):
    try:
        strs = input()
        print(strs)
        if strs == "":
            break
    except EOFError:
        break