from django.db import models

from django.contrib import admin 

class Student (models.Model):
    referencenumber = models.CharField(max_length=8,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email =models.EmailField()

class StudentAdmin(admin.ModelAdmin):
    list_display = ("referencenumber","name","age","email")
