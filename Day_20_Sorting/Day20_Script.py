def BubleSort(a):
    num_of_swaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                num_of_swaps+=1
    return [a[0],a[-1],num_of_swaps]


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    Info = BubleSort(a)
    print('Array is sorted in',str(Info[2]),'swaps.')
    print('First Element:',Info[0])
    print('Last Element:',Info[1])
