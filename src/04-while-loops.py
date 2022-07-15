
while True:
    N = int(input("Enter a number: "))

    # Check for positivity
    if N < 0:
        print("It is negative.")
    else:
        print("It is positive.")

    # Check for even/odd
    if N == 0:
        print("N is zero")
    elif N % 2 == 0:
        print("N is even")
    else:
        print("N is odd")

    print("")
