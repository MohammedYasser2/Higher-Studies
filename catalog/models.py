from atexit import register
from pickle import TRUE
from django.db import models

CASCADE = models.CASCADE



class Courses(models.Model):
    ID =  models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length= 25,null = True)
    dep = models.CharField(max_length=20,null = True)
    n_hours = models.IntegerField(null = True)
    hall_number = models.IntegerField(null = True)
    lectue_day = models.CharField(max_length=10,null = True)


    def __str__(self):
      return self.ID



class Students(models.Model):
    ID = models.CharField(max_length=8,primary_key = True)
    name = models.CharField(max_length= 25)
    birth = models.DateField()
    university = models.CharField(max_length=20,default='Cairo University')
    #gpa = models.DecimalField(max_digits= 4,decimal_places=2)
    gender = models.CharField(max_length=6)
    #level = models.IntegerField()
    is_active = models.BooleanField(default=True)
    dep = models.CharField(max_length=20)
    course1 =  models.ForeignKey(Courses, on_delete= CASCADE, null=True, related_name="course1")
    course2 =  models.ForeignKey(Courses, on_delete= CASCADE, null=True,related_name="course2")
    course3 =  models.ForeignKey(Courses, on_delete= CASCADE, null=True,related_name="course3")
    #register = models.ManyToManyField(Courses)
    def __str__(self):
        return self.ID

    class Meta:
        ordering = ['ID']    

'''
class Registration(models.Model):
    name = models.CharField(max_length=20,default='Student')
    student_ID = models.CharField(max_length=9,primary_key=TRUE)
    def __str__(self):
        return self.student_ID

    class Meta:
        ordering = ['student_ID']    
'''



