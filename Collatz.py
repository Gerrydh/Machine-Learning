# The number we will perform the Collatz operations on.
n = int(input("Enter a positive integer"))

# Keep looping until we reach 1. Note: this assunmes the collatz conjecture is true.
while n != 1:
    # Print the current value of n.
    print(n)
    # Check if n is even.
    if n % 2 == 0:
        # If n is even, divide by two.
        n = n / 2
    else:
        #if n is odd, multiply by 3 and add 1.
        n = (3 * n) + 1
# Finally print the 1.
print(n)
