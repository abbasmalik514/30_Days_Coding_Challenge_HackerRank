if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    i=len(arr)
    while(i>0):
        print(arr[i-1],end=' ')
        i-=1
