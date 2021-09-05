#recursive factorial function


def factorial(n):
    """This is a factorial recursive function"""
    if n==1:
        return 1
    else:
        return (n*factorial(n-1))

num = 3

print("Factorial of",num,"is",factorial(num))