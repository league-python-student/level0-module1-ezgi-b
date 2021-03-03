if __name__ == "__main__":
    for i in range(2):
        one = ""
        two = ""
        for j in range(12):
            one += "Badger"
            if j != 11:
               one += ", "
        for k in range(2):
            two += "Mushroom"
            if k != 1:
               two += ", "
        print(one)
        print(two)
    print("A Snake!!!")