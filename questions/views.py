from django.shortcuts import render, redirect
from questions.models import Question, Language, Framework
from questions.forms import QuestionForm, LanguageForm, FrameworkForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def question_list(request, id=None):
    if request.user.is_authenticated():
        framework = Framework.objects.get(id=id)
        questions = framework.questions.all()
        context = {
            'question_list': questions,
            'framework': framework,
        }
        return render(request, 'questions/question_list.html', context)
    return HttpResponse("You need to login first.")


def question_create(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        form = QuestionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            item = form.save(commit=False)
            # item.user = request.user
            item.save()
            # messages.success(request, "Successfully Created.")
            return redirect("questions:question-list", item.framework.id)
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
    return HttpResponse("You are not authorised to proceed")


def question_update(request, id=None):
    if request.user.is_authenticated() and request.user.is_superuser:
        question = Question.objects.get(id=id)
        if request.method == 'POST':
            form = QuestionForm(request.POST, instance=question)
            if form.is_valid():
                item = form.save(commit=False)
                question.question_text = item.question_text
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
        framework = question.framework.id
        question.delete()
        messages.success(request, "Successfully deleted.")
        return redirect("questions:question-list", framework)
    return HttpResponse("You are not authorised to proceed.")

def language_create(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        form = LanguageForm(request.POST or None)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return HttpResponseRedirect(item.get_absolute_url())
        context = {
            "form": form
        }
        return render(request, 'questions/language_form.html', context)
    return HttpResponse("You are not authorised to proceed.")

def language_list(request):
    if request.user.is_authenticated():
        languages = Language.objects.all()
        context = {
            'language_list': languages
        }
        return render(request, 'questions/language_list.html', context)
    return HttpResponse("You need to login first.")


def language_detail(request, id=None):
    if request.user.is_authenticated():
        language = Language.objects.get(id=id)
        frameworks = language.frameworks.all()
        context = {
            'frameworks': frameworks,
        }
        return render(request, 'questions/language_detail.html', context)
    return HttpResponse("You are not authorised to proceed")

def framework_create(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        form = FrameworkForm(request.POST or None)
        if form.is_valid():
            item = form.save()
            return redirect("questions:question-list", item.id)
        context = {
            "form": form
        }
        return render(request, 'questions/framework_form.html', context)
    return HttpResponse("You are not authorised to proceed.")
