class Student:
    def get_full_name(self):
        pass

    def get_contact_data(self):
        pass

    def is_adult(self):
        pass

    def get_results(self):
        pass


class Pupil:
    def __init__(self, first_name, last_name, email, age, grades):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._age = age
        self._grades = grades

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_age(self):
        return self._age

    def get_grades(self):
        return self._grades


class PupilAdapter(Student):
    def __init__(self, pupil: Pupil):
        self._pupil = pupil

    def get_full_name(self):
        return self._pupil.get_first_name() + ' ' + self._pupil.get_last_name()

    def get_contact_data(self):
        return self._pupil.get_email()

    def is_adult(self):
        return self._pupil.get_age() >= 18

    def get_results(self):
        return self._pupil.get_grades()


students = [
    PupilAdapter(Pupil('Jan', 'Kowalski', 'j@kowalski.pl', 19, [3, 4, 5, 2, 4])),
    PupilAdapter(Pupil('Maria', 'Deep', 'm@deep.pl', 17, [2, 4, 4, 2, 3])),
    PupilAdapter(Pupil('Joanna', 'Nowak', 'j@gmail.com', 21, [4, 4, 5, 4, 5]))
]

for student in students:
    print(f'Adult: {student.is_adult()}')
    print(f'Name: {student.get_full_name()}')
    print(f'Contact: {student.get_contact_data()}')
    print(f'Results: {student.get_results()}')


"""
Class version
"""


class Student:
    def get_full_name(self):
        pass

    def get_contact_data(self):
        pass

    def is_adult(self):
        pass

    def get_results(self):
        pass


class Pupil:
    def __init__(self, first_name, last_name, email, age, grades):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._age = age
        self._grades = grades

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_age(self):
        return self._age

    def get_grades(self):
        return self._grades


class PupilAdapter(Student, Pupil):
    def __init__(self, first_name, last_name, email, age, grades):
        super().__init__(first_name, last_name, email, age, grades)

    def get_full_name(self):
        return self.get_first_name() + ' ' + self.get_last_name()

    def get_contact_data(self):
        return self.get_email()

    def is_adult(self):
        return self.get_age() >= 18

    def get_results(self):
        return self.get_grades()


students = [
    PupilAdapter('Jan', 'Kowalski', 'j@kowalski.pl', 19, [3, 4, 5, 2, 4]),
    PupilAdapter('Maria', 'Deep', 'm@deep.pl', 17, [2, 4, 4, 2, 3]),
    PupilAdapter('Joanna', 'Nowak', 'j@gmail.com', 21, [4, 4, 5, 4, 5])
]

for student in students:
    print(f'Adult: {student.is_adult()}')
    print(f'Name: {student.get_full_name()}')
    print(f'Contact: {student.get_contact_data()}')
    print(f'Results: {student.get_results()}')
