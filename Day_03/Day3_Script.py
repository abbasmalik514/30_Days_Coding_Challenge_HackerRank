# Input should not be less than 1 and greater then 100
if __name__ == '__main__':
    N = int(input())
    if(N>0 and N<101):
        if (N%2!=0):
            print('Weird')
        elif N in range(1,6):
            print('Not Weird')
        elif N in range(5,21):
            print('Weird')
        elif N>20:
            print('Not Weird')
