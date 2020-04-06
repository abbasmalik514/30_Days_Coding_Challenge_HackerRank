class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idName,scores):
        super().__init__(firstName, lastName, idName)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        total_score=0
        for score in self.scores:
            total_score+=score
        average = total_score/len(self.scores)
        if 90<=average and average<=100:
            return 'O'
        elif 80<=average and average<90:
            return 'E'
        elif 70<=average and average<80:
            return 'A'
        elif 55<=average and average<70:
            return 'P'
        elif 40<=average and average<55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
