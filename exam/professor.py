# filename:     professor.py
# author:       dan.smith.me@gmail.com
# date:         06/08/2016
# version:      1.0
# =====================================================================================================================

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

# class ArrogantProfessor(Professor):
#     def say(self, stuff):
#         return self.name + ' says: ' + 'It is obvious that ' + Person.say(self, stuff)
#
#     def lecture(self, stuff):
#         return 'It is obvious that ' + Person.say(self, stuff)

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return Person.say(self, 'It is obvious that ' + Lecturer.lecture(self, stuff))

    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)



e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

# print(e.say('the sky is blue'))
# print(le.lecture('the sky is blue'))
print(pe.say('the sky is blue'))
# print(pe.lecture('the sky is blue'))
print(ae.say('the sky is blue'))
print(ae.lecture('the sky is blue'))
