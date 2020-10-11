import sys

sys.path.append("..")

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from backend.planner import Planner
from .models import Student
from src.backend.json_parser import JSONParser

def login(request: HttpRequest) -> HttpResponse:
    """
    :param request: To view the login page
    :return: The login page
    """
    return render(request, 'login.html', {})


def profile(request: HttpRequest) -> HttpResponse:
    """
    :param request: To view the profile page
    :return: The profile page
    """
    user = request.POST['studentID']
    password = request.POST['password']

    s1 = Student()
    s1.matric = "10157409"
    s1.password = "123456"
    s1.name = "Hamburglar"  
    s1.study_yr = "2"
    s1.course = "Computer Science"
    s1.mods_cleared = "CZ1001","CZ1002"
    s1.img = "https://cdn.dribbble.com/users/935504/screenshots/3123811/artboard.png"

    s2 = Student()
    s2.matric = "1922118"
    s2.password = "123456"
    s2.name = "Ronald MacDonald"
    s2.study_yr = "3"
    s2.course = "Computer Science"
    s2.mods_cleared = "CZ2001","CZ2002"
    s2.img = "https://cached.imagescaler.hbpl.co.uk/resize/scaleWidth/743/cached.offlinehbpl.hbpl.co.uk/news/OMC/C785C365-DB1F-ABBE-BEF5F76B8E2868E1.jpg"

    students = [s1,s2]

    for i in range (len(students)):
        if user == students[i].matric and password == students[i].password:
            s = students[i]
            return render(request, 'profile.html', {"s" : s})

    return render(request, 'login.html')


def timetable(request: HttpRequest) -> HttpResponse:
    """
    :param request: To view the timetable page
    :return: The timetable page
    """
    # context = {"d": {"s1": {"name": "FASHION & DESIGN: WEARABLE ART AS A SECOND SKIN*",
    #                         "au": " 3.0 AU",
    #                         "index": "aaaaaaaaaaa"},
    #                  "s2": {"name": "ART",
    #                         "au": " 3.0 AU",
    #                         "index": "aaaaaaaaaaa"},
    #                  "s3": {"name": "WEARABLE ART AS A SECOND SKIN*",
    #                         "au": " 3.0 AU",
    #                         "index": "aaaaaaaaaaa"}
    #                  }}
    # return render(request, 'timetable.html', context)

    # @SUNNY, CHANGE THIS LINE TO GENERATE COMBIS FOR DIFFERENT COURSES YOU WANNA PLAN FOR
    list = request.GET.getlist('course')
    data = {"combinations": Planner.generate_combis(list)}
    return render(request, 'timetable.html', data)

def search(request: HttpRequest) -> HttpResponse:
    """
    :param request: To view the search page
    :return: The search page
    """
    coursenames = ["CZ2001", "CZ2002", "CZ2003", "CZ2004", "CZ2005", "CZ2006"]
    return render(request, 'search.html', {"coursenames": coursenames})
