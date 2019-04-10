# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Student,Teacher
# Create your views here.
def details(request):
    name=request.POST.get("t1")
    age=request.POST.get("t2")
    group=request.POST.get("t3")
    Student(name=name,age=age,home_group=group).save()
    qs = Student.objects.all()
    return render(request,"index.html",{"qs":qs,"type":"student"})
def index(request):
    qs=Student.objects.all()
    return render(request,"index.html",{"qs":qs,"type":"student"})


def TeacherInfo(request):
    qs=Teacher.objects.all()
    return render(request,"index.html",{"type":"Teacher","qs1":qs,})


def Teacher_Details(request):
    name=request.POST.get("t1")
    age=request.POST.get("t2")
    contact=request.POST.get("t3")
    Teacher(name=name,age=age,contact=contact).save()
    qs = Teacher.objects.all()
    return render(request,"index.html",{"type":"Teacher","qs1":qs})