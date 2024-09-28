from groupLimitError import GroupLimitError

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.__counter = 0

    def add_student(self, student):
        if self.__counter < 10 :
            self.group.add(student)
            self.__counter += 1
        else: raise GroupLimitError()

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                self.__counter -= 1
                return self.group.discard(student)
        print("Student not found")
        return None

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        print("Student not found")
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'






