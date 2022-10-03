class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] # пройденные курсы
        self.courses_in_progress = [] # изучаемые курсы
        self.grades = {} # оценки
    
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_of_student:
                lecturer.grades_of_student[course] += [grade]
            else:
                lecturer.grades_of_student[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        a = 0
        b = 0
        for i in self.grades:
            a += sum(self.grades.get(i))
            b += len(self.grades.get(i))
        c = a / b
        return c

    def __str__(self):
        res = (f'Имя: {self.name}\n' 
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self._average_grade()}\n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self._average_grade() < other._average_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] # прикрепленные курсы
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_of_student = {}
                
    def _average_grade(self):
        a = 0
        b = 0
        for i in self.grades_of_student:
            a += sum(self.grades_of_student.get(i))
            b += len(self.grades_of_student.get(i))
        c = a / b
        return c

    def __str__(self):
        res = (f'Имя: {self.name}\n' 
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self._average_grade()}')
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self._average_grade() < other._average_grade()
        

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
            
    def __str__(self):
        res = (f'Имя: {self.name}\n' 
               f'Фамилия: {self.surname}')
        return res
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python', 'C++']

last_student = Student('John', 'Smith', 'your_gender')
last_student.finished_courses += ['Git']
last_student.courses_in_progress += ['Python', 'C++']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'C++']

cooler_reviewer = Reviewer('Every', 'One')
cooler_reviewer.courses_attached += ['Python', 'C++']

cool_lecturer = Lecturer('Peter', 'Ivanov')
cool_lecturer.courses_attached += ['C++']
cool_lecturer.courses_attached += ['Python']

cooler_lecturer = Lecturer('Vasya', 'Petrov')
cooler_lecturer.courses_attached += ['C++']
cooler_lecturer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'C++', 8)

cooler_reviewer.rate_hw(last_student, 'Python', 10)
cooler_reviewer.rate_hw(last_student, 'C++', 7)

best_student.rate_lect(cool_lecturer, 'C++', 7)
best_student.rate_lect(cool_lecturer, 'Python', 10)

last_student.rate_lect(cooler_lecturer, 'C++', 6)
last_student.rate_lect(cooler_lecturer, 'Python', 8)

print(cool_reviewer)
print()
print(cooler_reviewer)
print()

print(best_student)
print()
print(last_student)
print()
print(best_student < last_student)
print()

print(cool_lecturer)
print()
print(cooler_lecturer)
print()
print(cool_lecturer < cooler_lecturer)
print('_____________________________________________________________________')
print()

students = [best_student, last_student]
lecturers = [cool_lecturer, cooler_lecturer]

def average_student(students, course2):
    gr = 0
    for i in range(len(students)):
        if course2 in students[i].grades:
            gr += sum(students[i].grades.get(course2))
        else:
            print('Ошибка')
            return
    print(f'Средний балл за домашние задания по курсу: {course2} составляет {gr / len(students)}')
  
def average_lecturers(lecturers, course3):
    gr = 0
    for i in range(len(lecturers)):
        if course3 in lecturers[i].grades_of_student:
            gr += sum(lecturers[i].grades_of_student.get(course3))
        else:
            print('Ошибка')
            return
    print(f'Средний балл за лекции по курсу: {course3} составляет {gr / len(lecturers)}')
    
average_student(students, 'Python')               
average_lecturers(lecturers, 'C++')