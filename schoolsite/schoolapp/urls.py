from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("teacher",views.teacher,name="teacher"),
    path("contact",views.contact,name="contact"),
    path("courses/<int:id>",views.enroll,name="courses"),
   
    path("vehicle",views.velhicle,name="vehicle"),
    path("about",views.about,name="about"),
    path("login",views.login,name="login"),
    path("course",views.course,name="course"),
    path('add_course/', views.add_course, name='add_course'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('edit_teacher/<int:id>', views.update_teacher, name='edit_teacher'),
    path('delete_teacher/<int:id>', views.delete_teacher, name='delete_teacher'),
    path('delete_course/<int:id>', views.delete_course, name='delete_course'),
    path('edit_course/<int:id>', views.update_course, name='edit_course'),
]