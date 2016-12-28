from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib import admin
from django.contrib import messages
from .models import (CustomUser, Profile,
                     Skillset,
                     )
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.views.generic import (View,)
from .forms import (ProfileForm,
                    UserLoginForm,
                    SkillsetForm,
                    profile_formset,
                    Skillformset,
                    )
from django.contrib.auth import (login,
                                 logout,
                                 authenticate,
                                 )
from django.core.urlresolvers import reverse
from django.db.models import Q

# Create your views here.

def home(request):
    greeting = "Welcome"
    return render(request, 'recruits/home.html', {'greeting': greeting})


def profile_list(request):
    users = CustomUser.objects.all()
    if not request.user.is_authenticated():
        return redirect("recruits:login")
    if request.user.is_authenticated() and request.user.is_superuser:
        profiles = Profile.objects.all().order_by('-time')
    elif request.user.is_authenticated():
        profiles = Profile.objects.filter(user=request.user).order_by('-time')
    context = {
        'profiles': profiles,
        'users': users,
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

        formset = profile_formset(request.POST or None)
        profile = ProfileForm(request.POST or None, request.FILES or None)
        context = {
                "profile": profile,
                "skill": formset,
            }

        if profile.is_valid():
            if formset.is_valid():
                item = profile.save(commit=False)
                item.user = request.user
                item.save()

                for form in formset:
                    this = form.save(commit=False)
                    if this.skill == '':
                        break
                    this.profile = item
                    this.save()

                messages.success(request, "Successfully Created.")
                return HttpResponseRedirect(item.get_absolute_url())

        return render(request, 'recruits/profile_form.html', context)
    return redirect("recruits:login")



def profile_update(request, id=None):
    if request.user.is_authenticated():
        profile = Profile.objects.get(id=id)
        skill = profile.skills.all()

        if request.method == 'POST':
            form = ProfileForm(request.POST or None, request.FILES or None)
            # formset = profile_formset(request.POST or None)
            if form.is_valid():
                item = form.save(commit=False)
                profile.name = item.name
                profile.email = item.email
                profile.designation = item.designation
                profile.current_ctc = item.current_ctc
                profile.expected_ctc = item.expected_ctc
                profile.notice_period = item.notice_period
                profile.resume = item.resume
                profile.recording = item.recording
                profile.save()

            return HttpResponseRedirect(profile.get_absolute_url())
        else:
            form = ProfileForm(instance=profile)
            # formset = profile_formset(instance=profile)
        context = {
            "profile": profile,
            "form" : form,
        }
        return render(request, 'recruits/test_form.html', context)
    return redirect("recruits:login")


def profile_delete(request, id=None):
    if request.user.is_authenticated():
        profile = Profile.objects.get(id=id)
        if profile.user == request.user:
            profile.delete()
            messages.success(request, "Successfully deleted.")
            return render(request, "recruits/profile_delete.html", {})
        return redirect("recruits:profile-list")
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

def skillupdate_view(request, id=None):
    if request.user.is_authenticated():
        profile = Profile.objects.get(id=id)
        skills = profile.skills.all()
        if request.method=="POST":
            formset = profile_formset(request.POST, instance=profile)
            if formset.is_valid():
                for skill in skills:
                    for form in formset:
                        # print(skill)
                        item = form.save(commit=False)
                        print(form)
                        if skill.skill==item.skill and skill.exp==item.exp:
                            pass
                        elif skill.skill==item.skill:
                            print(item)
                            skill.exp = item.exp
                            pass
                        elif item.skill=='' or item.exp=='':
                            pass
                        else:
                            item.profile = profile
                            item.save()


                    return HttpResponseRedirect(profile.get_absolute_url())
        else:
            formset = profile_formset(queryset=skills)
        context = {
            "skills": skills,
            "formset": formset
        }
        return render(request, "recruits/skill_form.html", context)
    return redirect("recruits:login")


def consultancy_view(request):
    users = CustomUser.objects.all()
    context = {
        'profiles': users,
    }
    return render(request, 'recruits/profile_list.html', context)


def search_view(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            queryset = Profile.objects.all()
            if request.GET.get('where'):
                where = request.GET.get('where')
                queryset = queryset.filter(location__icontains=where).distinct()
            if request.GET.get('from'):
                how = request.GET.get('from')
                queryset = queryset.filter(skills__exp__gte=int(how)).distinct()
            if request.GET.get('to'):
                how = request.GET.get('to')
                queryset = queryset.filter(skills__exp__lte=int(how)).distinct()
            if request.GET.get('which'):
                which = request.GET.get('which')
                if 'python' in which:
                    queryset = queryset.python().distinct()
                elif 'javascript' in which:
                    queryset = queryset.javascript().distinct()
                else:
                    queryset = queryset.filter(skills__skill__icontains=which).distinct()
            queryset = queryset.order_by('-time')

            if not request.user.is_superuser:
                queryset = queryset.filter(user=request.user)

        context = {
        'profiles': queryset,
        # 'key': key,
            }
        return render(request, 'recruits/profile_list.html', context)
    return redirect("recruits:login")
