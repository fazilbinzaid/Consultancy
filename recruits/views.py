from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib import admin
from django.contrib import messages
from .models import (CustomUser, Profile,
                     Skillset,
                     )
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.generic import (View,
                                  ListView,
                                  DetailView,
                                  )
from .forms import (ProfileForm,
                    UserLoginForm,
                    SkillForm,
                    profile_formset,
                    )
from django.contrib.auth import (login,
                                 logout,
                                 authenticate,
                                 )
from django.core.urlresolvers import reverse

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        greeting = "Welcome"
        return render(request, 'recruits/home.html', {'greeting': greeting})


def profile_list(request):
    if not request.user.is_authenticated():
        return HttpResponse("You need to Login first.")
    if request.user.is_authenticated() and request.user.is_superuser:
        profiles = Profile.objects.all().order_by('user')
    elif request.user.is_authenticated():
        profiles = Profile.objects.filter(user=request.user)
    context = {
        'profile_list': profiles
    }
    return render(request, 'recruits/profile_list.html', context)



def profile_detail(request, id=None):
    if not request.user.is_authenticated():
        return HttpResponse("You need to Login first.")
    elif request.user.is_authenticated():
        profile = Profile.objects.get(id=id)
        context = {
            'profile': profile
        }
        return render(request, 'recruits/detail.html', context)


def profile_create(request):
    if request.user.is_authenticated():

        skill = profile_formset(request.POST or None)
        profile = ProfileForm(request.POST or None, request.FILES or None)
        context = {
                "profile": profile,
                "skill": skill,
            }
        if profile.is_valid():
            if skill.is_valid():
                item = profile.save(commit=False)
                item.user = request.user
                item.save()
                for form in skill:
                    this = form.save(commit=False)
                    this.profile = item
                    this.save()

            messages.success(request, "Successfully Created.")
            return HttpResponseRedirect(item.get_absolute_url())

        return render(request, 'recruits/profile_form.html', context)
    return redirect("recruits:login")



def profile_update(request, id=None):
    if request.user.is_authenticated():
        profile = Profile.objects.get(id=id)
        if request.method == 'POST':
            form = ProfileForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                item = form.save(commit=False)
                item.save()
                return HttpResponseRedirect(item.get_absolute_url())
        else:
            form = ProfileForm(instance=profile)
        context = {
            "form": form,
        }
        return render(request, 'recruits/profile_form.html', context)
    return HttpResponse("You need to Login first.")

def profile_delete(request, id=None):
    if request.user.is_authenticated():
        profile = Profile.objects.get(id=id)
        if profile.user == request.user:
            profile.delete()
            messages.success(request, "Successfully deleted.")
            return redirect("recruits:profile-list")
        return redirect("recruits:profile-detail")
    return HttpResponse("You need to Login first.")

def login_view(request):
    if not request.user.is_authenticated():
        title = "Login"
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            return HttpResponseRedirect(user.get_absolute_url())

        return render(request, 'recruits/form.html', { "form": form, "title": title })
    else:
        user = request.user
        return HttpResponseRedirect(user.get_absolute_url())

def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html", {})
    # return HttpResponseRedirect("recruits:home")
