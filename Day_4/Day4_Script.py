class Person:
    def __init__(self,initialAge):
        if (initialAge<0):
            print('Age is not valid, setting age to 0.')
            self.__age = 0
        else:
            self.__age = initialAge

    def amIOld(self):
        if (self.__age<13):
            print('You are young.')
        elif (self.__age>=13 and self.__age<18):
            print('You are a teenager.')
        else:
            print('You are old.')

    def yearPasses(self):
        self.__age+=1


if  __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        age = int(input())         
        person = Person(age)  
        person.amIOld()
        for j in range(0, 3):
            person.yearPasses()       
        person.amIOld()
        print("")
