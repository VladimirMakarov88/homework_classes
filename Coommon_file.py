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

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Вышла ошибочка'
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ох уж эти ошибки'
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return 'Все мы ошибаемся..'
        return self.average_grade() >= other.average_grade()


class Mentor():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
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

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Вышла ошибочка'
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ох уж эти ошибки'
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return 'Все мы ошибаемся..'
        return self.average_grade() >= other.average_grade()


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



# ВЫВОД ПО ДОМАШНЕМУ ЗАДАНИЮ № 1
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor))
print(isinstance(reviewer, Mentor))
print(lecturer.courses_attached)
print(reviewer.courses_attached)


# ВЫВОД ПО ДОМАШНЕМУ ЗАДАНИЮ № 2
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга')
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
print(lecturer.grades)  # {'Python': [7]}
print()


# ВЫВОД ПО ДОМАШНЕМУ ЗАДАНИЮ № 2
some_reviewer = Reviewer('Some', 'Buddy') # вывод для Проверяющих

some_lecturer = Lecturer('Some', 'Buddy') # вывод для Лекторов
some_lecturer.grades = {'Python': [6, 5, 4, 8]}

some_student = Student('Ruoy', 'Eman') # вывод для Студентов
some_student.grades = {'Python': [10, 7, 8, 9], 'C++': [5, 7, 6, 9], 'JavaScript': [9, 8, 8, 4], 'Visual Basic': [8, 3]}
some_student.courses_in_progress = ['Python', 'C++', 'JavaScript', 'Visual Basic']
some_student.finished_courses = ['Введение в программирование на языке Python']

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)


# ВЫВОД ПО ДОМАШНЕМУ ЗАДАНИЮ № 3
some_reviewer1 = Reviewer('Some', 'Buddy') # вывод для Проверяющих (два экземпляра)
some_reviewer2 = Reviewer('Any', 'Times')

some_lecturer1 = Lecturer('Andrew', 'Ivanov') # вывод для Лекторов (два экземпяра)
some_lecturer1.grades = {'Python': [6, 5, 4, 8]}
some_lecturer1.courses_attached = ['TypeScript']
some_lecturer2 = Lecturer('Sergey', 'Menshov')
some_lecturer2.courses_attached = ['C++', 'Python']
some_lecturer2.grades = {'C++': [6, 5, 4, 8], 'Python': [6, 8, 9, 8]}

some_student1 = Student('Ruoy', 'Eman') # вывод для Студентов
some_student1.grades = {'C++': [5, 7, 6, 9], 'JavaScript': [9, 8, 8, 4]}
some_student1.courses_in_progress = ['C++', 'JavaScript']
some_student1.finished_courses = ['Введение в программирование на языке Python']

some_student2 = Student('Vladimir', 'Stepanov')
some_student2.grades = {'Java': [2, 8, 6, 9], 'TypeScript': [9, 7, 8, 3]}
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
print()

for course in all_courses:
    for student in student_list:
        if course in student.grades:
            student_average = sum(student.grades[course]) / len(student.grades[course])
            print(f'Средняя оценка у студента {student.name} {student.surname} по языку {course}: {student_average}')

print()

# ПРОВЕРКА сравнения средних оценок через методы сравнения.
print(f'Средние оценки студента: {some_student1.name} {some_student1.surname} = '
      f'средним оценкам студента: {some_student2.name} {some_student2.surname}? '
      f'{some_student1 == some_student2}')

print(f'Средние оценки студента: {some_student1.name} {some_student1.surname} < '
      f'средним оценкам студента: {some_student2.name} {some_student2.surname}? '
      f'{some_student1 < some_student2}')

print(f'Средние оценки студента: {some_student1.name} {some_student1.surname} > '
      f'средним оценкам студента: {some_student2.name} {some_student2.surname}? '
      f'{some_student1 > some_student2}')

print(f'Средние оценки студента: {some_student1.name} {some_student1.surname} >= '
      f'средним оценкам студента: {some_student2.name} {some_student2.surname}? '
      f'{some_student1 >= some_student2}')

print(f'Средние оценки студента: {some_student1.name} {some_student1.surname} <= '
      f'средним оценкам студента: {some_student2.name} {some_student2.surname}? '
      f'{some_student1 <= some_student2}')

print()
print(f'Средние оценки Лектора: {some_lecturer1.name} {some_lecturer1.surname} = '
      f'средним оценкам лектора: {some_lecturer2.name} {some_lecturer2.surname}? '
      f'{some_lecturer1 == some_lecturer2}')

print(f'Средние оценки Лектора: {some_lecturer1.name} {some_lecturer1.surname} < '
      f'средним оценкам лектора: {some_lecturer2.name} {some_lecturer2.surname}? '
      f'{some_lecturer1 < some_lecturer2}')

print(f'Средние оценки Лектора: {some_lecturer1.name} {some_lecturer1.surname} > '
      f'средним оценкам лектора: {some_lecturer2.name} {some_lecturer2.surname}? '
      f'{some_lecturer1 > some_lecturer2}')

print(f'Средние оценки Лектора: {some_lecturer1.name} {some_lecturer1.surname} >= '
      f'средним оценкам лектора: {some_lecturer2.name} {some_lecturer2.surname}? '
      f'{some_lecturer1 >= some_lecturer2}')

print(f'Средние оценки Лектора: {some_lecturer1.name} {some_lecturer1.surname} <= '
      f'средним оценкам лектора: {some_lecturer2.name} {some_lecturer2.surname}? '
      f'{some_lecturer1 <= some_lecturer2}')


