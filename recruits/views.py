from django.shortcuts import render
from .models import (Consultancy, Profile,
                     Skillset,
                     )
from django.http import HttpResponseRedirect
from django.views.generic import (View,
                                  ListView,
                                  DetailView,
                                  )
from .forms import ProfileForm

# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):
        greeting = "Welcome"
        return render(request, 'recruits/home.html', {'greeting': greeting})

class ProfileListView(ListView):
    model = Profile
    template_name = 'recruits/profile_list.html'
    context_object_name = 'profile_list'

class ProfileDetailView(View):
    model = Profile
    queryset = Profile.objects.all()
    # context_object_name = 'profile'

    def get(self, request, id, format=None):
        prof = Profile.objects.get(pk=id)
        context = {'profile': prof}
        return render(request, 'recruits/profile_detail.html', context)


def profile_create(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.save()
        return HttpResponseRedirect(item.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, 'recruits/profile_form.html', context)

def profile_update(request, id):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.save()
        return HttpResponseRedirect(item.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, 'recruits/profile_form.html', context)


# class ProfileView(View):
#     form_class = ProfileForm
#     template_name = "recruits/profile-view.html"
#     initial = {'key': 'value'}
#
#     def get(self, request, *args, **kwargs):
#         queryset = Profile.objects.all()
#         form
