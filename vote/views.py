from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from vote.models import Question


def home(request):
    return HttpResponse("welcome to Vote Page")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/datails.html", {question: question})


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question doesn't exist")
#     return HttpResponse("You're looking at question %s." % question)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return render(request, 'index_vote.html', context={"vote_list": latest_question_list})
