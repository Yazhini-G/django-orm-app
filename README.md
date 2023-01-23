# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram


![orm](https://user-images.githubusercontent.com/120244201/214110001-e347edd3-c4dc-4499-bf4e-1e5614aa8eaf.jpg)

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
serverside output

![2023-01-23 (5)](https://user-images.githubusercontent.com/120244201/214110309-ff45bb95-1022-4769-a88c-c1f764e8f070.jpg)

clientsideoutput


![2023-01-23 (4)](https://user-images.githubusercontent.com/120244201/214110414-dec08343-9ecb-4b9e-8918-f1427dafab51.jpg)


## RESULT
And thus we created our orm model.
