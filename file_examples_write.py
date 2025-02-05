# lets create a virtual diary
with open("diary.txt", "a") as fp: # w = writing, a = amending
    while True:
        text = input("How do you feel today? (type q to quit): ")
        if text == "q":
            break
        fp.write(f"{text}\n")


