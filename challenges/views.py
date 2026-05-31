from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    response_content = ""
    for month in months:
        link = reverse("monthly-challenge", args=[month])
        response_content+= f'<li><a href="{link}">{month.capitalize()}</a></li>'
    
    response_content = f"<ul>{response_content}</ul>"
    return HttpResponse(response_content)


monthly_challenges = {
    "january": "Walk for at least 20 minutes every day.",
    "february": "Read one new book this month.",
    "march": "Try a new recipe each week.",
    "april": "Spend 10 minutes daily journaling.",
    "may": "Practice a new skill for 15 minutes each day.",
    "june": "Complete a short workout three times a week.",
    "july": "Unplug from screens for one hour every evening.",
    "august": "Learn a new word every day.",
    "september": "Organize one area of your home each weekend.",
    "october": "Write down one thing you are grateful for daily.",
    "november": "Try a new hobby this month.",
    "december": "Reflect on the year and set one goal for next year.",
}


def month_by_number(request, month: int):
    if not (0 < month < 13):
        return HttpResponseNotFound(f"There is no month with the number {month}!")
    months = list(monthly_challenges.keys())
    month_str = months[month - 1]
    return HttpResponseRedirect(
        reverse("monthly-challenge", kwargs={"month": month_str})
    )


def month_by_str(request, month: str):
    month = month.lower()
    challenge_text = monthly_challenges.get(month)
    if challenge_text is None:
        return HttpResponseNotFound(f"There is no month called {month}!")
    return HttpResponse(challenge_text)
