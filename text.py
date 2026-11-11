class course:
    def  init  (self,course_name,teacher_name,capacity):
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.capacity = capacity
        self.students =  []

def  register__student(self,student__name):
    if student__name in self.students:
        print("دانشجو قبلا ثبت نام   کرده است")
    elif len(self.students) >= self.capacity:
        print("ظرفیت کلاس تکمیل است")
    else:
        self.students.append(student__name)
        print("ثبت نام باموفقیت انجام شد")
def remove__student(self, student__name):
    if student__name in self.students:
        self.students.remove(student__name)
        print("دانشجو حذف شد")
    else:
         print("دانشجو    یافت نشد")
          
def show_students(self):
    print("لیست دانشجویان:")
    for  student in self.students:
         print(student)

def remaining_capacity(self):
    return self.capacity - len(self.students)

def __str__(self):
    return f"{self.course_name}{self.teacher_name}{self.capacity}"
    course1 = course("python","ali",3)
    course2 = course("html","sara"5)
    course1.register__student("nesa")
    course1.register__student("maryam")
    course1.register__student("sara")
    print(course1)
    course1.show_students()
    print("remaining:",course1.remaining_capacity())
    course1.remove__student("maryam")
    print(course1)