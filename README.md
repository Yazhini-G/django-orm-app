# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram



## DESIGN STEPS

### STEP 1:
Start a django project 
### STEP 2:
create super user

### STEP 3:
make migrations and runserver


## PROGRAM :
### models. py:
```
from django.db import models

from django.contrib import admin 

class Student (models.Model):
    referencenumber = models.CharField(max_length=8,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email =models.EmailField()

class StudentAdmin(admin.ModelAdmin):
    list_display = ("referencenumber","name","age","email")
```

### admin. py:
```
from django.contrib import admin

from .models import Student,StudentAdmin

admin.site.register(Student,StudentAdmin)
```




## OUTPUT




## RESULT
And thus we created our orm model.