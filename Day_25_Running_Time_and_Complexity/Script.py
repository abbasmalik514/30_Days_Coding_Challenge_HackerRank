from math import sqrt

def checkPrime(data):
    if data==1:
        return 'Not prime'

    for i in range(2,int(sqrt(data))+1):
        if data%(i)==0:
            return 'Not prime'
    return 'Prime'


if __name__=="__main__":
    T=int(input())
    for i in range(T):
        data=int(input())
        print(checkPrime(data))
