from django.db import models
from django.urls import reverse

class school(models.Model):
    School_Name = models.CharField(max_length=50, help_text='School Name')
    School_Address = models.CharField(max_length=100, help_text='School Address')
    School_Telephone = models.CharField(max_length=20, help_text='Telephone')
    School_Email = models.EmailField()

    def __str__(self):
        return self.School_Name
    
    def get_absolute_url(self):
        return reverse('school-detail-view', args=[str(self.id)])

class ClassName(models.Model):
    ClassName = models.CharField(max_length=20, help_text='Class Name')
    schoolID = models.ForeignKey('school', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.ClassName
    
    def get_absolute_url (self):
        return reverse('class-detail', args=[str(self.id)])
    
class student(models.Model):
    Student_First_Name = models.CharField(max_length=20, help_text='First Name')
    Student_Last_Name = models.CharField(max_length=20, help_text='Last Name')
    student_dateOfBirth = models.DateField()
    Gen = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    student_gender = models.CharField(max_length=10, choices=Gen)
    schoolID = models.ForeignKey('school', on_delete=models.CASCADE, null=True)
    classID = models.ForeignKey('ClassName', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.Student_First_Name} {self.Student_Last_Name}"

class teacher(models.Model):
    teacher_firstName = models.CharField(max_length=20, help_text='Teacher First Name')
    teacher_lastName = models.CharField(max_length=20, help_text='Teacher Last Name')
    teacher_email = models.EmailField()
    Ext = (
        ('mr', 'Mr.'),
        ('ms', 'Ms.'),
        ('miss', 'Miss')
    )
    extension = models.CharField(max_length=10, choices=Ext)
    classID = models.ManyToManyField('ClassName')

    def __str__(self):
        return f"{self.extension} {self.teacher_lastName}"

