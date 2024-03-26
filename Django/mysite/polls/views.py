from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
#from django.views import generic
from .forms import QuestionForm, VoteForm

from .models import Choice, Question


# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"
#     def get_queryset(self):
#         return Question.objects.order_by("-pub_date")[:6]


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:7]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = "polls/results.html"

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse("polls:results", args=(question.id,)))
    

def new_poll(request):
    if request.method=='POST':
        q_form=QuestionForm(request.POST)
        if q_form.is_valid():
            question=q_form.save()
            return redirect('polls:add_choice', question_id=question.pk)
    else:
        q_form=QuestionForm()
    return render(request,'polls/new_poll.html',context={'q_form':q_form})
    

def add_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            #choice=form.save()
            choice = form.save(commit=False)
            choice.question = question
            choice.save()
            
            return redirect('polls:add_choice', question_id=question.id)
    else:
        form = VoteForm()
    return render(request, 'polls/add_choice.html', {'form': form, 'question': question})

def delete_poll(request,question_id):
    question=get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect(reverse('polls:index'))

def delete_choice(request,choice_id):
    choice=get_object_or_404(Choice,pk=choice_id)
    question_id=choice.question.id
    choice.delete()
    return redirect(reverse('polls:detail', args=(question_id,)))
    
