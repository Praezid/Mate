def parity_checker() -> None:
    # write your code here
    number  = int(input("What number do you want to check?"))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
