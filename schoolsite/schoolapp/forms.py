from django import forms
from . models import *
class Category_Forms(forms.ModelForm):
     class Meta:
        model=Category
        fields='__all__'
        widgets={
            'name':forms.TextInput(),
            }
        
class Course_Forms(forms.ModelForm):
     class Meta:
        model=Course
        fields='__all__'
        widgets={
                "title": forms.TextInput(),
        "description" : forms.TextInput(),
        "instructor" : forms.Select(),
        "start_date" : forms.DateInput(),
        "category" : forms.Select()  ,
        "imageCourse": forms.FileInput(),
        "end_date" :  forms.DateInput(),
        "available_seats" : forms.NumberInput(),
        "duration" : forms.NumberInput(),
        "price" : forms.NumberInput(),
        }

class Instructor_Form(forms.ModelForm):
    class Meta:
        model=Instructor
        fields='__all__'
        widgets={
       "name" : forms.TextInput(attrs={'class':'col-lg-12'}),
       "email" : forms.EmailInput(attrs={'class':'col-lg-12'}),
      "bio" : forms.TextInput(attrs={'class':'col-lg-12'}),
    "specialty" : forms.TextInput(attrs={'class':'col-lg-12'}),
    "imageInstructor": forms.FileInput(),
        }
class Student_Form(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={


       "name" : forms.TextInput(attrs={'class':'col-lg-12'}),
       "email" : forms.EmailInput(attrs={'class':'col-lg-12'}),
      "phone" : forms.TextInput(attrs={'class':'col-lg-12'}),
   
        }
class Enrollment_Form(forms.ModelForm):
    class Meta:
        model=Enrollment
        fields='__all__'
        widgets={
    #        student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # enrollment_date = models.DateTimeField(auto_now_add=True),

       "student" : forms.Select(),
       "course" : forms.Select(),
      "enrollment_date" : forms.DateInput(),
   
        }