def display():
    n=10

    def inner():
        nonlocal n
        n+=10
        print("Inner function: ",n)
    inner()
    print("Outer Function:",n)

display()
