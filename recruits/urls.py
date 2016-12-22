from .views import (Home,
                    profile_list,
                    profile_detail,
                    profile_create,
                    profile_update,
                    profile_delete,
                    login_view,
                    logout_view,
                    skillupdate_view,
                    consultancy_view,
                    search_view,
                    )
from django.conf.urls import include, url



urlpatterns = [

        url(r'profiles/$', profile_list, name='profile-list'),
        url(r'profiles/(?P<id>[0-9]{1,2})/$', profile_detail, name='profile-detail'),
        url(r'profiles/create/$', profile_create, name='profile-create'),
        url(r'profiles/(?P<id>[0-9]{1,2})/update/$', profile_update, name='profile-update'),
        url(r'profiles/(?P<id>[0-9]{1,2})/delete/$', profile_delete, name='profile-delete'),
        url(r'login/$', login_view, name='login'),
        url(r'logout/$', logout_view, name='logout'),
        url(r'skill-update/(?P<id>[0-9]{1,2})/$', skillupdate_view, name='skill-update'),
        url(r'home/$', Home.as_view(), name='home'),
        url(r'users/$', consultancy_view, name='consultancy'),
        url(r'search/$', search_view, name='search'),


]
