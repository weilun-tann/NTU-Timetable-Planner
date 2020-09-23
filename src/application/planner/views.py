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
    context = {"d": {"s1":{"name":"FASHION & DESIGN: WEARABLE ART AS A SECOND SKIN*",
                    "au":" 3.0 AU",
                    "index":"aaaaaaaaaaa"},
               "s2": {"name": "ART",
                      "au": " 3.0 AU",
                      "index": "aaaaaaaaaaa"},
               "s3": {"name": "WEARABLE ART AS A SECOND SKIN*",
                      "au": " 3.0 AU",
                      "index": "aaaaaaaaaaa"}
               }}
    return render(request, 'timetable.html', context)
