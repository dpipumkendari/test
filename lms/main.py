from lms.course import Course
from lms.student import Student


def main() -> None:
    """Demonstrate simple LMS operations."""
    course = Course(name="Math 101", description="Introductory mathematics")
    alice = Student(name="Alice")
    bob = Student(name="Bob")

    alice.enroll(course)
    bob.enroll(course)

    print(course)
    print(alice)
    print(bob)


if __name__ == "__main__":
    main()
