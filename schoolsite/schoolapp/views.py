from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import  Login
from django.contrib import messages
from .models import * 
from . forms import *
from datetime import datetime
# Create your views here.
hide=0
def index(request):
    global hide
   
    context={
        "teachers":Instructor.objects.all(),
        "courses":Course.objects.all(),
         "hide":hide,
    }
  
    return render(request,'pages/index.html',context)




def add_course(request):
    if request.method == 'POST':
        add_book=Course_Forms(request.POST,request.FILES,)
        if add_book.is_valid():
            add_book.save()
            return redirect('course')

    context={
        "formCourse":Course_Forms(),
    }
    return render(request, 'pages/add_course.html',context) 



def add_teacher(request):
    if request.method == 'POST':
        add_book=Instructor_Form(request.POST,request.FILES,)
        if add_book.is_valid():
            add_book.save()
            return redirect('teacher')

    context={
        "formTeacher":Instructor_Form(),
    }
    return render(request, 'pages/add_teacher.html',context)  


def add_category(request):
    if request.method == 'POST':
        add_cate=Category_Forms(request.POST)
        if add_cate.is_valid():
            add_cate.save()
            return redirect('course')

    context={
        "formCate":Category_Forms(),
    }
    return render(request, 'pages/add_category.html',context)  



def course(request):
    context={
        "courses":Course.objects.all(),
        "category":Category.objects.all(),
        "hide":hide,
       
    }
   
    return render(request,'pages/course.html',context)
def teacher(request):
    context={
        "teachers":Instructor.objects.all(),
        "hide":hide,
    }
    return render(request,'pages/teacher.html',context)
def enroll(request,id):
   
    course_id=Course.objects.get(id=id)
    course = get_object_or_404(Course, id=id)
  
  
    if request.method == 'POST':
        add_student=Student_Form(request.POST)
        if add_student.is_valid():
            studentName=add_student.save()
        if course.remaining_seats > 0:
          
            enrollment=Enrollment(student=studentName,course=course_id,enrollment_date=datetime.now())
            enrollment.save()
            return redirect('index')
        else:
             messages.error(request,'No seats available in this course.')
             return redirect('course')
           
      

    context={
        'nameCourse':course_id,
        'enroll':Student_Form(),
      
    }
   
 
    return render(request,'pages/enroll.html',context)


def velhicle(request):
    return render(request,'pages/vehicle.html',)
def contact(request):
    return render(request,'pages/contact.html',)
def about(request):
    return render(request,'pages/about.html',)
def login(request):
    if request.method =='POST':
    
       user = request.POST.get('email')
       password=request.POST.get('password')
      
       if Login.objects.filter(username=user) and Login.objects.filter(password=password) :
           global hide
           hide = Login.objects.filter(type="admin").count()
         
           context={
               "hide":hide,
           }
         
           return render(request,'pages/index.html',context)
       else:
           messages.error(request,'User is not exists')
   
           
    return render(request,'pages/login.html',)
    



def update_teacher(request,id):
    teacher_id=Instructor.objects.get(id=id)
    if request.method=='POST':
        teacher_save=Instructor_Form(request.POST,request.FILES,instance=teacher_id)
        if(teacher_save.is_valid()):
            teacher_save.save()
            return redirect('teacher')
    else:
        teacher_save=Instructor_Form(instance=teacher_id)
    context={'form':teacher_save}
    
    return render(request,"pages/edit_teacher.html",context)

def update_course(request,id):
    course_id=Course.objects.get(id=id)
    if request.method=='POST':
        course_save=Course_Forms(request.POST,request.FILES,instance=course_id)
        if(course_save.is_valid()):
            course_save.save()
            return redirect('course')
    else:
        course_save=Course_Forms(instance=course_id)
    context={'form':course_save}
    
    return render(request,"pages/edit_course.html",context)



def delete_teacher(request,id):
    teacher_id=get_object_or_404(Instructor,id=id)
    if request.method=='POST': 
        teacher_id.delete()
        return redirect('teacher')
    return render(request,"pages/delete_teacher.html",)


def delete_course(request,id):
    course_id=get_object_or_404(Course,id=id)
    if request.method=='POST': 
        course_id.delete()
        return redirect('course')
    return render(request,"pages/delete_course.html",)




