from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


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
    return render(request, 'profile.html', {})


def timetable(request: HttpRequest) -> HttpResponse:
    """
    :param request: To view the timetable page
    :return: The timetable page
    """
    return render(request, 'timetable.html', {})
