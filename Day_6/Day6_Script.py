if __name__ == "__main__":
    T = int(input())
    strings = {}
    for i in range(T):
        strings[i] = str(input())
    for i in range(T):    
        j=0
        while (j<len(strings[i])):
            print('{0}'.format(strings[i][j]), end="")
            j+=2
        print(' ',end="")
        j=1
        while (j<len(strings[i])):
            print('{0}'.format(strings[i][j]), end="")
            j+=2
        print()
