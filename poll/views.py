from django.http import HttpResponse
from django.shortcuts import render

# 127.0.0.1:8000/poll
def index(request):
    return HttpResponse("안녕하세요~ django")

#127.0.0.1:8000/poll/1
def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)