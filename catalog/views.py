from ast import Return
from email.policy import default
from unicodedata import category
from django.shortcuts import render
from django.http import JsonResponse
import json

#from urllib3 import HTTPResponse
from .models import Courses, Students
from django.shortcuts import get_object_or_404



def index(request):
    return render(request, 'catalog/index.html')
def index8(request):
    return render(request, 'catalog/index8.html')    

def edit(request):
    return render(request, 'catalog/edit.html')

def addStudent(request):
    if (request.method == "POST"):
        ID = request.POST.get('ID')
        name = request.POST.get('name')
        university = request.POST.get('university')
        department = request.POST.get('department')
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        is_active = request.POST.get('status').lower() == 'active'
        course1 = request.POST.get('course1')
        course2 = request.POST.get('course2')
        course3 = request.POST.get('course3')
        data = Students(ID = ID,
                        name=name,
                        university=university,
                        dep=department,
                        birth=date,
                        gender=gender,
                        is_active=is_active,
                        course1=Courses.objects.filter(ID=course1)[0],
                        course2=Courses.objects.filter(ID=course2)[0],
                        course3=Courses.objects.filter(ID=course3)[0],
        )
        data.save()
        return index(request)

    context = {
        'courses' : Courses.objects.all()
    }
    return render(request,'catalog/add-student.html', context=context)


def getStudents(request):
   context = {
       'stu' : Students.objects.all()
   }
   return render(request,'catalog\StudentsT.html', context=context)


def addCourse(request):
   
        ID = request.POST.get('ID')
        name = request.POST.get('name')
        department = request.POST.get('department')
        n_hours = request.POST.get('n_hours')
        hall_number = request.POST.get('hall_number')
        lectue_day = request.POST.get('lectue_day')
        data = Courses(ID = ID,
                        name=name,
                        dep=department,
                        n_hours=n_hours,
                        lectue_day=lectue_day,
                        hall_number=hall_number,
        )
        data.save()
        return render(request,'catalog/add-course.html')


def regCourse(request):
    if (request.method == "POST"):
        ID = request.POST.get('ID')
        name = request.POST.get('name')
       # course = request.POST.get('course')
        data = Students(ID = ID, name = name)
        data.save()
        context = {
        'courses' : Courses.objects.all()
         }
        return render(request,'catalog/course-reg.html',context = context)
        
    return render(request,'catalog/course-reg.html')



def search(request):
    if (request.method == "POST"):
          id = request.POST.get('ID')
          context = {
              'student': Students.objects.get(ID = id)
              } 
          return render(request,'catalog/search.html', context=context) 
    return render(request,'catalog/index4.html')  



def deleteCourse(request):
     if (request.method == "POST"):
         ID = request.POST.get('ID')
         course = Courses.objects.get(ID = ID) 
         course.delete()
         return index(request)
     return render(request,'catalog/del-course.html')  



def deleteStudent(request):
     if (request.method == "POST"):
         ID = request.POST.get('ID')
         student = Students.objects.get(ID = ID) 
         student.delete()
         return index(request)
     return render(request,'catalog/del-student.html')  

def editCourse(request):
    if (request.method == "POST"):
      id = request.POST.get('edit')
      ID = request.POST.get('ID')
      name = request.POST.get('name')
      department = request.POST.get('department')
      n_hours = request.POST.get('n_hours')
      hall_number = request.POST.get('hall_number')
      lectue_day = request.POST.get('lectue_day')
      course = Courses.objects.get(ID = id)
      course = get_object_or_404(Courses, ID= id)
      course.ID = ID
      course.name = name
      course.dep =department
      course.n_hours = n_hours
      course.hall_number = hall_number
      course.lectue_day = lectue_day
      course.save()
      Courses.objects.get(ID = id).delete()

      return index(request)
    return render(request,'catalog/edit-course.html')    
       



def editStudent(request):
    if (request.method == "POST"):
        id = request.POST.get('edit')
        ID = request.POST.get('ID')
        name = request.POST.get('name')
        university = request.POST.get('university')
        department = request.POST.get('department')
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        student = Students.objects.get(ID = id)
        student = get_object_or_404(Students, ID= id)
        student.ID = ID
        student.name = name
        student.university = university
        student.dep = department
        student.date = date
        student.gender = gender
        student.save()
        student = Students.objects.get(ID = id).delete()
        return index(request)
    return render(request,'catalog/edit-student.html')