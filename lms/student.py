class Student:
    """Represents a student in the LMS."""

    def __init__(self, name: str):
        self.name = name
        self.courses = []

    def enroll(self, course: "Course") -> None:
        if course not in self.courses:
            self.courses.append(course)
            course.enroll(self)

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, courses={len(self.courses)})"
