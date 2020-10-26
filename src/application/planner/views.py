import sys

sys.path.append("..")
import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from backend.cache import TimetableCombinationsCache
from backend.planner import Planner
from .models import Student
from backend.json_parser import JSONParser
from backend.entities import CustomJSONEncoder
from .forms import UserLogIn

# TO CACHE PREVIOUSLY QUERIED COMBINATIONS
timetable_cache = TimetableCombinationsCache()


def loginUser(request: HttpRequest) -> HttpResponse:
    """
    :param request: To view the login page
    :return: The login page
    """

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Username/Password incorrect')
    form = UserLogIn
    return render(request, 'login.html', {'forms' : form })


def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='home')
def profile(request: HttpRequest) -> HttpResponse:
    """
    :param request: To view the profile page
    :return: The profile page
    """

    s1 = Student()
    s1.matric = "U1922118L"
    s1.name = "Aik Yu Chen"
    s1.study_yr = "2"
    s1.course = "Computer Science"
    s1.mods_cleared = "CZ1011", "CZ1012", "CZ1007", "MH1812"
    s1.img = "https://cdn.dribbble.com/users/935504/screenshots/3123811/artboard.png"

    return render(request, 'profile.html', {"s": s1})


@login_required(login_url='home')
def timetable(request: HttpRequest) -> HttpResponse:
    """
    :param request: To view the timetable page
    :return: The timetable page
    """
    course_indexes = [L.split()[0] for L in request.GET.getlist('course')]
    combinations = timetable_cache.get(course_indexes) or Planner.generate_combis(course_indexes)
    timetable_cache.set(course_indexes, combinations)
    return render(request, 'timetable.html', {"combinations": combinations})


@login_required(login_url='home')
def alt_indexes(request: HttpRequest) -> HttpResponse:
    clicked_index = request.POST["clickedIndex"]
    combi = json.loads(request.POST["combi"])
    alt_idxes = Planner.get_alt_indexes(clicked_index, combi)
    return JsonResponse({'alt_indexes': json.dumps(alt_idxes, cls=CustomJSONEncoder)})


@login_required(login_url='home')
def search(request: HttpRequest) -> HttpResponse:
    """
    :param request: To view the search page
    :return: The search page
    """
    coursecodes = JSONParser.get_course_names()
    # coursenames = ["CZ2001", "CZ2002", "CZ2003", "CZ2004", "CZ2005", "CZ2006"]
    return render(request, 'search.html', {"coursecodes": coursecodes})
