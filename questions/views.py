from django.shortcuts import render
from questions.models import Question
from questions.forms import QuestionForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def question_list(request):
    if request.user.is_authenticated():
        questions = Question.objects.all()
        context = {
            'question_list': questions
        }
        return render(request, 'questions/question_list.html', context)
    return HttpResponse("You need to login first.")


def question_create(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        form = QuestionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, "Successfully Created.")
            return HttpResponseRedirect(item.get_absolute_url())
        context = {
            "form": form,
        }
        return render(request, 'questions/question_form.html', context)
    return HttpResponse("You are not authorised to proceed.")


def question_detail(request, id=None):
    if request.user.is_authenticated():
        question = Question.objects.get(id=id)
        context = {
            'question': question
        }
        return render(request, 'questions/question_detail.html', context)
    return HttpResponse("You need to login first.")


def question_update(request, id=None):
    if request.user.is_authenticated() and request.user.is_superuser:
        question = Question.objects.get(id=id)
        if request.method == 'POST':
            form = QuestionForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                item = form.save(commit=False)
                item.save()
                return HttpResponseRedirect(item.get_absolute_url())
        else:
            form = QuestionForm(instance=question)
        context = {
            "form": form,
        }
        return render(request, 'questions/question_form.html', context)
    return HttpResponse("You are not authorised to proceed.")

def question_delete(request, id=None):
    if request.user.is_authenticated() and request.user.is_superuser:
        question = Question.objects.get(id=id)
        if question.user == request.user:
            question.delete()
            messages.success(request, "Successfully deleted.")
            return redirect("questions:question-list")
        return redirect("questions:question-detail")
    return HttpResponse("You are not authorised to proceed.")
