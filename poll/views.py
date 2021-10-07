from django.http import HttpResponse
from django.shortcuts import render
from poll.models import Question

#127.0.0.1:8000/poll - 전체 목록
def index(request):
    question_list = Question.objects.all
    return render(request, 'poll/index.html', {'question_list': question_list})

    #return HttpResponse("안녕하세요~ django")

#127.0.0.1:8000/poll/1 - 1개 정보
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'poll/detail.html', {'question': question})

    #return HttpResponse("You are looking at question %s." % question_id)