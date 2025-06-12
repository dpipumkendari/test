class Course:
    """Represents a course in the LMS."""

    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.students = []

    def enroll(self, student: "Student") -> None:
        if student not in self.students:
            self.students.append(student)

    def __repr__(self) -> str:
        return f"Course(name={self.name!r}, students={len(self.students)})"
