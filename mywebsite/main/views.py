from django.shortcuts import render
from datetime import datetime
import random
from .models import Submission

def get_dynamic_content():
    quotes = [
        "Life is what happens when you're busy making other plans.",
        "The purpose of our lives is to be happy.",
        "Life is short, and it's up to you to make it sweet.",
        "Live in the sunshine, swim the sea, drink the wild air."
    ]
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_quote = random.choice(quotes)
    return {
        "current_datetime": current_datetime,
        "random_quote": random_quote
    }

def home(request):
    dynamic_content = get_dynamic_content()
    return render(request, 'index.html', dynamic_content)

def submit_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        submission = Submission(name=name, email=email)
        submission.save()
        submitted_data = {
            "name": name,
            "email": email
        }
        dynamic_content = get_dynamic_content()
        dynamic_content["submitted_data"] = submitted_data
        return render(request, 'index.html', dynamic_content)
    else:
        return render(request, 'index.html', get_dynamic_content())

def submissions_list(request):
    submissions = Submission.objects.all()
    return render(request, 'submissions.html', {'submissions': submissions})

