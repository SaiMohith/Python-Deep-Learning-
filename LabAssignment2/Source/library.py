#  This program is to create a School Management System


class SchoolMember:  # Parent Class School Member (1st Class)
    num_of_school_members = 0
    num_of_students = 0
    num_of_teachers = 0
    __name_of_school = "UMKC"  # Private Data Member

    def __init__(self, name):  # init constructor
        self.name = name  # self
        print(name, "is a school member of", SchoolMember.__name_of_school)  # displays school members

    def display_teacher_info(self, name, course):  # displays teacher informarion
        self.name = name
        self.course = course
        print(name, "is instructor for", course)

    def display_ra_info(self, name, professor):  # displays RA information
        self.name = name
        self.professor = professor
        print(name, "works under", professor, "as RA")

    def display_st_info(self, name):  # displays Student information
        self.name = name
        print(name, "is Student")

    def add_member(self, i):
        SchoolMember.num_of_school_members += i

    def add_student(self, i):
        SchoolMember.num_of_students += i

    def add_teacher(self, i):
        SchoolMember.num_of_teachers += i


class Grade:  # Another parent class for getting the Grade (2nd Class)

    def __init__(self, g):  # init constructor
        self.g = g
        if self.g in range(90, 101):
            print("Grade is A. Outstanding!")
        elif self.g in range(80, 90):
            print("Grade is A-. Excellent!")
        elif self.g in range(70, 80):
            print("Grade is B. Good!")
        elif self.g in range(60, 70):
            print("Grade is B-. Average!")
        elif self.g in range(50, 60):
            print("Grade is C. Below Average!")
        else:
            print("Grade is F. Study Hard!")


class Teacher(SchoolMember):  # Single Inheritance (3rd Class)

    def __init__(self, name, dep, c, suffix):  # init constructor
        self.name = name
        self.dep = dep
        self.c = c
        self.suffix = suffix
        print("\nName:", name, ('({})'.format(suffix)), "\nDept:", dep)
        super().__init__(name)  # Super call for SchoolMember
        super().display_teacher_info(name, c)
        super().add_member(1)
        super().add_teacher(1)


class Student(SchoolMember, Grade):  # Multiple Inheritance (4th Class). Inherits SchoolMember and Grade Classes

    def __init__(self, name, dep, id, grade):  # init constructor
        self.name = name
        self.dep = dep
        self.id = id
        self.grade = grade
        print("\nName:", name, "\nID:", id, "\nDept:", dep)
        super().__init__(name)  # Super call for SchoolMember
        super().display_st_info(name)
        Grade(grade)  # calls the Grade Class
        super().add_member(1)
        super().add_student(1)


class RA(Student):  # 5th Class. It inherits Student Class

    def __init__(self, name, dep, id, grade, prof):  # init constructor
        self.name = name
        self.id = id
        self.dep = dep
        self.grade = grade
        self.prof = prof
        super().__init__(name, dep, id, grade)  # Super call for Student
        super().display_ra_info(name, prof)  # also inherits the Schoolmember class


# Studeent Instance
st1 = Student("Mohith", "CS", "16233203", 95)
st2 = Student("Minh", "Communication", "18646537", 49)

# Teacher Instance
t1 = Teacher("YugYung Lee", "CS", "Python & BigData", "Ph.D")
t2 = Teacher("Yjie Han", "CS", "Parallel Algorithms", "Ph.D")

# RA Instance
r1 = RA("Rashmi", "CSE", "9274827", 91, "Lee")
r2 = RA("Dig Vijay", "CS", "91746292", 98, "Praveen Rao")

# School Member Instance
print("\n")
sm = SchoolMember("Jack")

# Grade Instance
print("\n")
gd = Grade(89)

print("\n")
print("Number of School Members:", SchoolMember.num_of_school_members)
print("Number of Students:", SchoolMember.num_of_students)
print("Number of Teachers:", SchoolMember.num_of_teachers)
