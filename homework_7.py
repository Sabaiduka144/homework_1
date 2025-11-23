import math
import datetime as dt
from random import randint as roll

PI_TWO_DECIMALS = round(math.pi, 2)

def current_utc():
    return dt.datetime.now(dt.timezone.utc)

def roll_die(sides=6):
    return roll(1, sides)

print("Task 1 Demonstration:")
print("PI_TWO_DECIMALS:", PI_TWO_DECIMALS)
print("Current UTC time:", current_utc())
print("Two dice rolls:", roll_die(), roll_die())
print()

def announce(event, *audiences, prefix="[INFO]"):
    audience_list = ", ".join(audiences) if audiences else "everyone"
    print(f"{prefix} {event} for {audience_list}")

def average_score(*scores):
    if not scores:
        raise ValueError("No scores provided")
    return round(sum(scores) / len(scores), 1)

def build_connection(host, *, port=5432, **credentials):
    connection = {"host": host, "port": port}
    connection.update(credentials)
    return connection

print("Task 2 Demonstration:")
announce("Meeting", "Team A", "Team B")
announce("Lunch break")
print("Average score:", average_score(80, 90, 75))
print("Average score:", average_score(100, 85))
conn1 = build_connection("localhost")
conn2 = build_connection("db.server.com", port=3306, user="admin", password="secret")
print("Connection 1:", conn1)
print("Connection 2:", conn2)
print()

def enroll_student(name, /, *, course, level="beginner", **meta):
    return {"name": name, "course": course, "level": level, **meta}

print("Task 3 Demonstration:")
student1 = enroll_student("Alice", course="Python Basics")
student2 = enroll_student("Bob", course="Data Science", level="intermediate")
student3 = enroll_student("Charlie", course="Web Dev", level="advanced", scholarship=True)
print(student1)
print(student2)
print(student3)

print()

class Course:
    def __init__(self, title, capacity):
        self.title = title
        self.capacity = capacity
        self.students = []

    def enroll(self, student):
        if len(self.students) >= self.capacity:
            raise ValueError(f"Course {self.title} is full!")
        self.students.append(student)

    def roster(self):
        return ", ".join(self.students) if self.students else "No students yet"

    def __repr__(self):
        return f"<Course: {self.title}, {len(self.students)}/{self.capacity} students>"

class OnlineCourse(Course):
    def __init__(self, title, capacity, platform):
        super().__init__(title, capacity)
        self.platform = platform

    def info(self):
        return f"{self.title} on {self.platform} ({len(self.students)}/{self.capacity} students)"

print("Task 4 Demonstration:")
course = Course("Python Foundations", 3)
course.enroll("Alice")
course.enroll("Bob")
print(repr(course))
print("Roster:", course.roster())

online_course = OnlineCourse("Data Science 101", 2, "Zoom")
online_course.enroll("Charlie")
print(repr(online_course))
print("Roster:", online_course.roster())
print("Info:", online_course.info())
print()

def course_report(*courses, **filters):
    min_capacity = filters.get("min_capacity", 0)
    platform_filter = filters.get("platform", None)

    for course in courses:
        if getattr(course, "capacity", 0) < min_capacity:
            continue
        if platform_filter and getattr(course, "platform", None) != platform_filter:
            continue
        announce(f"Course Report: {course.title}", prefix="[REPORT]")
        print("  Info:", getattr(course, "info", lambda: f"{course.title} ({len(course.students)}/{course.capacity} students)")())
        print("  Roster:", course.roster())
        print()

print("Optional Stretch Demonstration:")
course_report(course, online_course)
course_report(course, online_course, min_capacity=3)
course_report(course, online_course, platform="Zoom")
