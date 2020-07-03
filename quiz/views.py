# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'quiz/index.html', context={
        "categories": categories,
    })

def play(request, category_id):
    quizzes = Quiz.objects.filter(category__id=category_id)
    options = list()

    for quiz in quizzes:
        current_options = Option.objects.filter(quiz__id=quiz.id)
        current_options_name = [option.text for option in current_options]
        options.append(current_options_name)

    return render(request, 'quiz/quiz.html', context={
        "quizzes": quizzes,
        "options": options,
    })

# def submit(request):
#     quiz