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

# вывод для Проверяющих
some_reviewer = Reviewer('Some', 'Buddy')

# вывод для Лекторов
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades = {'Python': [6, 5, 4, 8]}

# вывод для Студентов
some_student = Student('Ruoy', 'Eman')
some_student.grades = {'Python': [10, 7, 8, 9], 'C++': [5, 7, 6, 9], 'JavaScript': [9, 8, 8, 4], 'Visual Basic': [8, 3]}
some_student.courses_in_progress = ['Python', 'C++', 'JavaScript', 'Visual Basic']
some_student.finished_courses = ['Введение в программирование на языке Python']


print(some_reviewer)
print(some_lecturer)
print(some_student)