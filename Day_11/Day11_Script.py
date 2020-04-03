def get_sum(arr,row,col):
    return arr[row][col]+arr[row][col+1]+arr[row][col+2]+arr[row+1][col+1]+arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum=-1000
    row=0
    col=0
    cont=1

    for i in range(16):
        if cont%5==0:
            row+=1
            col=0
            cont=1
        cont+=1
        temp_sum=get_sum(arr,row,col)
        col+=1
        
        if temp_sum>max_sum:
            max_sum=temp_sum
        temp_sum=-10
    
    print(max_sum)
