list = []
def insert(firstNameEmailID):
    if len(list)==0:
        list.append(firstNameEmailID)
        return 0
    else:
        for i in range(len(list)):
            if firstNameEmailID[0][0]<=list[i][0][0]:
                list.insert(i,firstNameEmailID)
                return 0
        list.append(firstNameEmailID)
        return 0

def print_list():
    for firstNameEmailId in list:
        print(firstNameEmailId[0])

if __name__ == '__main__':
    N = int(input())
    for N_itr in range(N):
        firstNameEmailID = input().split()

        if '@gmail' in firstNameEmailID[1]:
            insert(firstNameEmailID)
    print_list()
