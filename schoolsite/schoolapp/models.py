from django.db import models

# Create your models here.
class Login(models.Model):
    typeUser=[
        ('admin','admin'),
        ('user','user')
              ]
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    type=models.CharField(max_length=10,choices=typeUser)
    def __str__(self) -> str:
        return self.username



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False,null=False)
    bio = models.TextField(blank=True,null=True)
    specialty = models.CharField(max_length=50)
    imageInstructor= models.ImageField(upload_to='photos/Instructor',null=True,blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=" Description",max_length=400)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE,null=True)
    start_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    imageCourse= models.ImageField(upload_to='photos',null=True,blank=True)
    end_date = models.DateField(blank=False,null=False,auto_now=True)
    available_seats = models.IntegerField(null=False,default=0)
    duration = models.IntegerField(help_text="Duration in hours",default=1,blank=False,null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title
    @property
    def remaining_seats(self):
        enrolled_students = Enrollment.objects.filter(course=self).count()
        return self.available_seats - enrolled_students

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False,null=False)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.course.title}"






