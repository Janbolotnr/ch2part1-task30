def element():
    word = input("Your word: ")
    elem = input("Which element: ")
    a = 0
    for i in word:
        if i == elem:
            a += 1
    print("Your element in the word:", a , "times")
element()