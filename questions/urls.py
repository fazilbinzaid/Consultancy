from .views import (question_list,
                    question_detail,
                    question_create,
                    question_update,
                    question_delete,
                    language_create,
                    language_list,
                    language_detail,
                    framework_create,
                    )
from django.conf.urls import include, url



urlpatterns = [

        url(r'frameworks/(?P<id>[0-9]+)/questions/$', question_list, name='question-list'),
        url(r'questions/(?P<id>[0-9]+)/$', question_detail, name='question-detail'),
        url(r'questions/create/$', question_create, name='question-create'),
        url(r'questions/(?P<id>[0-9]+)/update/$', question_update, name='question-update'),
        url(r'questions/(?P<id>[0-9]+)/delete/$', question_delete, name='question-delete'),
        url(r'languages/create/$', language_create, name='language-create'),
        url(r'languages/$', language_list, name='language-list'),
        url(r'languages/(?P<id>[0-9]+)/$', language_detail, name='language-detail'),
        url(r'frameworks/create/$', framework_create, name='framework-create'),


]
