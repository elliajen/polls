from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from poll.models import Question

# 127.0.0.1:8000/poll - 전체 목록
def index(request):
    question_list = Question.objects.all
    return render(request, 'poll/index.html', {'question_list': question_list})

    # return HttpResponse("안녕하세요~ django")

# 127.0.0.1:8000/poll/1 - 1개 정보
def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'poll/detail.html', {'question': question})

    # return HttpResponse("You are looking at question %s." % question_id)

# 127.0.0.1:8000/poll/2/vote
def vote(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        choice = request.POST['choice'] # name에서 가져오기
        sel_choice = question.choice_set.get(id=choice)
    except KeyError:
        return render(request,'poll/detail.html', {'question': question, 'error_message': '선택을 해주세요'})
    else:
        sel_choice.votes += 1
        sel_choice.save()
        return HttpResponseRedirect(reverse('poll:result',args=(question.id,)))

# 127.0.0.1:8000/poll/2/results
def result(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'poll/result.html', {'question':question})