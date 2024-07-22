from django.shortcuts import render, redirect
from .models import Question,Choice,Vote
from django.contrib import messages


# Create your views here.

def polls_home(request):
    questions = Question.objects.all()
    return render(request, 'polls_home.html',{'questions': questions})


def vote(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    #if request.method == 'POST':
    #    inputvalue = request.POST['choice']
    #    selection_option = options.get(id=inputvalue)
    #    selection_option.vote += 5
    #    selection_option.save()
    return render(request, 'vote.html',{'question':question, 'options':options})




def result(request,pk):
    poll = Question.objects.get(id=pk)
    options = poll.choices.all()
    if request.method == 'POST':
        if Vote.objects.filter(question=poll, voter=request.user).exists():
            messages.error(request,"You already voted in this poll")
            return redirect("polls_home")
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 1
        selection_option.save()
        Vote.objects.create(voter=request.user,question=poll)
    return render(request, 'result.html',{'poll':poll, 'options':options})


        
        
        



