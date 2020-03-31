
def binary(n):
    binary_n = str(n%2)
    if n>1:
        binary_n = binary(int(n/2))+binary_n
    return binary_n 

def max_consective_ones(binary_n):
    counter=0
    max_count=0
    for digit in binary_n:
        if digit == '0':
            if counter>max_count:
                max_count=counter
            counter = 0
        else:
            counter+=1
    if counter>max_count:
        max_count = counter
    return max_count

if __name__ == '__main__':
    n = int(input())
    binary_n = binary(n)
    print(max_consective_ones(binary_n))
