from django.contrib import admin
from .models import school, student, ClassName, teacher

admin.site.register(school)
admin.site.register(student)
admin.site.register(ClassName)
admin.site.register(teacher)

