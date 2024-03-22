'''
1) Класс книга
'''
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def info(self):
#         print(f'Название: {self.title}\n'
#               f'Автор: {self.author}\n'
#               f'Кол-во страниц: {self.pages}')
    
#     def size(self):
#         if self.pages > 300:
#             print('Книга большая')
#         else:
#             print('Книга маленикая')
        
# book1 = Book('Грокаем алгоритмы', 'Адитья Бхаргава', 290)
# book1.info()
# book1.size()

'''
2) Класс студент
'''
# class Student:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.grate = None

#     def set_grade(self, grade):
#         self.grate = grade

#     def get_grade(self):
#         if self.grate is None:
#             print(f'У студента не проставлена оценка!')
#         else:
#             print('Оценка студента: {self.grade}')


# student1 = Student('Daniiar')
# student1.get_grade()
# student1.set_grade(83)    
# student1.get_grade()

'''
3) Наследование - Класс Преподаватель
'''

class Teacher:
    def __init__(self, name, subjekct):
        self.name = name
        self.subject = subjekct

    def info(self):
        print(f'{self.name}Предмет преподавания {self.subject}')

class TeacherMath(Teacher):
    pass

class TeacherLang(Teacher):
    pass

teachr_math = TeacherMath(name='Фибоначчи', subjekct='Математик')
teachr_lang = TeacherLang(name='Гвидо Ван Россум', subjekct='python')

teachr_math.info()
teachr_lang.info()