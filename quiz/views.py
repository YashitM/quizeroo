# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
@login_required
def index(request):
    categories = Category.objects.all()
    return render(request, 'quiz/index.html', context={
        "categories": categories,
    })

def check_correct_option(recvd_option, quiz_id):
    choices = Option.objects.filter(quiz__id=quiz_id)
    
    for choice in choices:
        if choice.correct:
            if recvd_option == choice.text:
                return True
    
    return False

@login_required
def play(request, category_id):
    quizzes = Quiz.objects.filter(category__id=category_id)
    options = list()
    correct_counters = list()

    for quiz in quizzes:
        current_options = Option.objects.filter(quiz__id=quiz.id)
        correct_counter = 0

        for counter in range(len(current_options)):
            if current_options[counter].correct:
                correct_counter = counter
                break
        
        correct_counters.append(correct_counter)
        current_options_name = [option.text for option in current_options]
        options.append(current_options_name)

    print(correct_counters)
    quizzes = quizzes[:15]
    options = options[:15]

    if request.method == "POST":
        score = request.POST.get('score', '')
        current_user_id = request.user.id

        profile = Profile.objects.filter(user__id = current_user_id).count()

        if profile != 0:
            current_profile = Profile.objects.get(user__id = current_user_id)
        else:
            current_profile = Profile()
            current_profile.user = request.user

        current_profile.score += int(score)
        current_profile.save()
        
        return redirect(leaderboard)

    return render(request, 'quiz/quiz.html', context={
        "quizzes": quizzes,
        "options": options,
        "correct_counters": correct_counters,
    })

def leaderboard(request):
    ordered_profiles = Profile.objects.order_by('-score')[:10]
    print(ordered_profiles)
    return render(request, 'quiz/leaderboard.html', context={
        "sorted_profiles": ordered_profiles,
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

