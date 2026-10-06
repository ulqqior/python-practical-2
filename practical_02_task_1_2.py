from collections import namedtuple

Student = namedtuple("Student", ["name", "grade"])

class StudentGroupIterator:
    """Ітератор для обходу StudentGroup."""
    
    def __init__(self, students: list[Student]):
        self._students = students
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Student:
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student

class StudentGroup:
    """Ітерабельний контейнер з колекцією студентів."""
    
    def __init__(self, students: list[Student]):
        self._students = students

    def __iter__(self):
        return StudentGroupIterator(self._students)

    def top_students(self, limit: int = 3):
        sorted_students = sorted(self._students, key=lambda s: s.grade, reverse=True)
        for i in range(min(limit, len(sorted_students))):
            yield sorted_students[i]

def main():
    group = StudentGroup([
        Student("Олена", 95),
        Student("Іван", 78),
        Student("Марія", 92),
        Student("Петро", 85)
    ])

    print("Всі пари студентів:")
    for s1 in group:
        for s2 in group:
            if s1.name < s2.name:
                print(f" {s1.name} та {s2.name}")

    print("\nТоп-3 студенти:")
    for student in group.top_students(3):
        print(f" {student.name}: {student.grade}")

if __name__ == "__main__":
    main()