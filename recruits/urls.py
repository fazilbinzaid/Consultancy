from .views import (Home,
                    ProfileListView,
                    ProfileDetailView,
                    profile_create,
                    profile_update,
                    )
from django.conf.urls import include, url



urlpatterns = [

        url(r'home/$', Home.as_view(), name='home'),
        url(r'profiles/$', ProfileListView.as_view(), name='profile-list'),
        url(r'profiles/(?P<id>[0-9]+)/$', ProfileDetailView.as_view(), name='profile-detail'),
        url(r'profiles/create/$', profile_create, name='profile-create'),
        url(r'profiles/update/(?P<id>[0-9]+)/$', profile_update, name='profile-update'),

]
