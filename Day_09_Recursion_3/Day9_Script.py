import os

# Complete the factorial function below.
def factorial(n):
    fact = 1
    if(n!=1):
        fact = factorial(n-1)
    return fact*n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
