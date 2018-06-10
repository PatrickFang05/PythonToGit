class Student:
    domain = 'gmail.com'
    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade

    def getEmail(self):
        email = self.first + '.' + self.last + '.' + '05' + self.domain
        return email

    def compareGrade(self, anotherStudent):
        anotherStudent = student2
        if self.grade > student2.grade:
            return self.first + ' ' + self.last + ' ' + 'has a better grade than' + ' ' + student2.first + ' ' + student2.last
        elif self.grade == student2.grade:
            return self.first + ' ' + self.last + ' ' + 'has the same grade as' + ' ' + student2.first + ' ' + student2.last
        else:
            return self.first + ' ' + self.last + ' ' + 'has a worse grade than' + ' ' + student2.first + ' ' + student2.last
student1 = Student('patrick', 'fang', 100 )
student2 = Student('justin', 'xiang', 100)
print(student1.grade)
print(student2.first, student2.last)
print(student1.compareGrade(student2))
