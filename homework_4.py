class Student():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # сборка вывода для Студентов
    def __str__(self):
        av_grade = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress) # склеиваем изучаемые курсы
        finished_courses = ', '.join(self.finished_courses)  # склеиваем завершенные курсы
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {av_grade}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    # средняя оценка
    def average_grade(self):
        all_grades = []
        for grade_list in self.grades.values():
            for grade in grade_list:
                all_grades.append(grade)
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0


    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in lecturer.courses_attached and
                course in self.courses_in_progress and
                1 <= grade <= 10):

            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    # вывод для Лектора
    def __str__(self):
        av_grade = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {av_grade}')

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            for grade in grades_list:
                all_grades.append(grade)
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # вывод для Проверяющего
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# функция средней оценки за домашние задания у двух разных экземпляров класса
def average_grade_student(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    return sum(all_grades) / len(all_grades)

# функция средней оценки за лекции лекторов у двух разных экземпляров класса
def average_grade_lector(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    return sum(all_grades) / len(all_grades)


# вывод для Проверяющих (два экземпляра)
some_reviewer1 = Reviewer('Some', 'Buddy')
some_reviewer2 = Reviewer('Any', 'Times')

# вывод для Лекторов (два экземпяра)
some_lecturer1 = Lecturer('Andrew', 'Ivanov')
some_lecturer1.grades = {'Python': [6, 5, 4, 8]}
some_lecturer1.courses_attached = ['TypeScript']
some_lecturer2 = Lecturer('Sergey', 'Menshov')
some_lecturer2.courses_attached = ['C++', 'Python']
some_lecturer2.grades = {'C++': [6, 5, 4, 8], 'Python': [6, 8, 9, 8]}


# вывод для Студентов
some_student1 = Student('Ruoy', 'Eman')
some_student1.grades = {'C++': [5, 7, 6, 9], 'JavaScript': [9, 8, 8, 4]}
some_student1.courses_in_progress = ['C++', 'JavaScript']
some_student1.finished_courses = ['Введение в программирование на языке Python']

some_student2 = Student('Vladimir', 'Stepanov')
some_student2.grades = {'Java': [5, 8, 6, 9], 'TypeScript': [9, 7, 8, 4]}
some_student2.courses_in_progress = ['Java', 'TypeScript']
some_student2.finished_courses = ['Введение в программирование на языке C++']


student_list = [some_student1, some_student2]
all_courses = some_student1.courses_in_progress + some_student2.courses_in_progress

lecturer_list = [some_lecturer1, some_lecturer2]
all_lecturer_courses = some_lecturer1.courses_attached + some_lecturer2.courses_attached


print(some_reviewer1)
print(some_reviewer2)
print()

print(some_lecturer1)
print(some_lecturer2)
for course in all_lecturer_courses:
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            lecturer_average = sum(lecturer.grades[course]) / len(lecturer.grades[course])
            print(f'Средняя оценка лектора {lecturer.name} {lecturer.surname} по языку {course}: {lecturer_average}')
print()

print(some_student1)
print(some_student2)
for course in all_courses:
    for student in student_list:
        if course in student.grades:
            student_average = sum(student.grades[course]) / len(student.grades[course])
            print(f'Средняя оценка у студента {student.name} {student.surname} по языку {course}: {student_average}')