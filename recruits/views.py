from django.shortcuts import render
from django.contrib import messages
from .models import (CustomUser, Profile,
                    #  Skillset,
                     )
from django.http import HttpResponseRedirect, Http404
from django.views.generic import (View,
                                  ListView,
                                  DetailView,
                                  )
from .forms import (ProfileForm,
                    UserLoginForm,
                    )
from django.contrib.auth import (authenticate,
                                 login,
                                 logout,
                                 )
from django.core.urlresolvers import reverse

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        greeting = "Welcome"
        return render(request, 'recruits/home.html', {'greeting': greeting})


def profile_list(request):
    if request.user.is_authenticated():
        profiles = Profile.objects.filter(user=request.user)
        context = {
            'profile_list': profiles
        }
        return render(request, 'recruits/profile_list.html', context)
    return Http404


def profile_detail(request, id=None):
    if request.user.is_authenticated():
        profile = Profile.objects.get(id=id)
        context = {
            'profile': profile
        }
        return render(request, 'recruits/detail.html', context)
    return Http404


def profile_create(request):
    if request.user.is_authenticated():
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, "Successfully Created.")
            return HttpResponseRedirect(item.get_absolute_url())
        context = {
            "form": form,
        }
        return render(request, 'recruits/profile_form.html', context)
    return Http404


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
    return Http404

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
