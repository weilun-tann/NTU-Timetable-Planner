from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ..planner import Planner


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
<<<<<<< Updated upstream
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
=======

    # @SUNNY, CHANGE THIS LINE TO GENERATE COMBIS FOR DIFFERENT COURSES YOU WANNA PLAN FOR
    data = {"combinations": Planner.generate_combis(["CZ2001", "CZ2002", "CZ2003", "CZ2004", "CZ2005", "CZ2006"])}
    return render(request, 'timetable.html', data)
>>>>>>> Stashed changes
