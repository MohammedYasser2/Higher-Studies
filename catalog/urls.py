from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
     path('index8/',views.index8, name='index8'),
    path('register-student', views.addStudent, name="add-student"),
    path('students/', views.getStudents, name="Students"),
    path('add-courses/',views.addCourse,name = "add-course"),
    path('StudentsTable/',views.getStudents,name = "StudentsT"),
    path('course-reg/',views.regCourse,name = "course-reg"),
    path('search/',views.search,name = "index4"),
    path('search_result',views.search,name = "search"),
    path('del-courses/',views.deleteCourse,name = "del-course"),
    path('edit-course/',views.editCourse,name = "edit-course"),
    path('edit-student/',views.editStudent,name = "edit-student"),
    path('del-student/',views.deleteStudent,name = "del-student"),
    path('edit/',views.edit,name = "edit")
]