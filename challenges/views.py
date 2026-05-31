from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):
    return HttpResponse("Challenges Home Page")


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


def month(request, month: str):
    month = month.lower()
    challenge_text = monthly_challenges.get(month)
    if challenge_text is None:
        return HttpResponseNotFound(f"There is no month called {month}!")
    return HttpResponse(challenge_text)
