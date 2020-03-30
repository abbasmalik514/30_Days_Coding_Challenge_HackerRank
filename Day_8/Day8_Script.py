if __name__ == '__main__':
    n = int(input())
    dict = {}
    for i in range(n):
        string=input().split()
        dict[string[0]] = string[1]
    while(True):
        try:
            query=input()
        except EOFError:
            break
        if query in dict:
            print(  query+"="+dict[query])
        else:
            print('Not found')
