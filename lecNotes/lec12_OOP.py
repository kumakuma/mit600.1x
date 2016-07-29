# filename:     lec12_OOP
# author:       dan.smith.me@gmail.com
# date:         24/07/2016
# version:      1.0
# =====================================================================================================================

# inheritance
import datetime

class Person(object):
    def __init__(self, name):
        """Create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)


    def getAge(self):
        """Return self's current age in days"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """ Return True if self's name is lexicographically
            less than other's name, False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    # other methods

    def __str__(self):
        """return self's name"""
        return self.name


# me = Person('Dan Caleb Smith')
# her = Person('Chie Miyadera')
# me.setBirthday(10,19,1978)
# her.setBirthday(10,15,1967)
# plist = [me, her]
# print plist
# for p in plist: print p
# plist.sort()
# for p in plist: print p


class MITPerson(Person):
    nextIDNum = 0 # nexd ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialise person attributes
        # new MIT attribute: a unique id number
        self.idNum = MITPerson.nextIDNum
        MITPerson.nextIDNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their id number, not name
    def __lt__(self, other):
        return self.idNum < other.idNum



# p1 = MITPerson('Eric')
# p2 = MITPerson('John')
# p3 = MITPerson('John')
# p4 = Person('John')
#
# print p1
# print p1.getIdNum()
# print p2.getIdNum()
# print p1 < p2
# print p3 < p2
#
# mlist = [p1,p2,p3,p4]
# mlist.sort()
# for p in mlist: print p


# L12 Problem 1
class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print self.incantation


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print spell

# spell = Accio()
# spell.execute()
# studySpell(spell)
# studySpell(Confundo())


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)



#  example = GradeBook
class Grades(object):
    """ A mapping from students to a list of grades"""
    def __init__(self):
        """ Create empty gradebook"""
        self.students = []  # list of Student objects
        self.grades = {}  # maps idNum -> list of grades
        self.isSorted = True  # true if self.students is sorted

    def addStudent(self, student):
        """ Assumes student is of type Student
            Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """ Assumes grade is a float
            add grade to the ist of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """ Return list of grades for student"""
        try:  # return copy of students grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    # def allStudents(self):
    #     """ Return a list of the students in the grade book"""
    #     if not self.isSorted:
    #         self.students.sort()
    #         self.isSorted = True
    #     # return copy of the list of students
    #     return self.students[:]

    #  Improved allStudents method using generator
    #  loop yields one at a time.  rather than returning a copy of whole list
    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s

def gradeReport(course):
    """ Assumes: course is of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append((str(s) + ' has no grades'))
        return '\n'.join(report)

# # test
# ug1 = UG('Jane Doe', 2014)
# ug2 = UG('John Doe', 2015)
# ug3 = UG('David Henry', 2003)
# g1 = Grad('John Henry')
# g2 = Grad('George Steinbrenner')
#
# six00 = Grades()
# six00.addStudent(g1)
# six00.addStudent(ug2)
# six00.addStudent(ug1)
# six00.addStudent(g2)
#
# for s in six00.allStudents():
#     six00.addGrade(s, 75)
# six00.addGrade(g1, 100)
# six00.addGrade(g2, 25)
#
# six00.addStudent(ug3)


#  Generators
def genFib():
    fibn_1 = 1   # fib(n-1)
    fibn_2 = 0   # fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next


# foo = genFib()
# for n in range(100):
#     print(foo.next())

# see above for improved allStudents method

# L12 P5 - genPrimes
def genPrimes():
    next = 2
    primes = [next]
    yield primes[-1]
    while True:
        next += 1
        r = True
        for p in primes:
            if next % p == 0:
                r = False
        if r:
            primes.append(next)
            yield primes[-1]

foo = genPrimes()
for i in range(10):
    num = foo.next()
    # if i%10 == 0:
    #     print num
    print num


def doubleDays(days):
    res = 1
    while days > 0:
        res *= 2
        days -= 1
    return res

print doubleDays(30)